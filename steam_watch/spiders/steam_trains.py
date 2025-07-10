import scrapy
from datetime import datetime, timedelta, timezone
import re

HEADCODE_PATTERN = re.compile(r"[15]Z\d{2}")
KNOWN_TOCS = {"WR", "SLC", "SRHC", "RTC", "UKRT"}


class SteamTrainsSpider(scrapy.Spider):
    name = "steam_trains"
    allowed_domains = ["realtimetrains.co.uk"]

    days_ahead = 7

    def __init__(self, station_code, **kwargs):
        super().__init__(**kwargs)
        self.station_code = station_code.upper()

    def start_requests(self):
        today = datetime.today()
        for i in range(self.days_ahead):
            check_date = today + timedelta(days=i)
            date_str = check_date.strftime("%Y-%m-%d")
            url = f"https://www.realtimetrains.co.uk/search/detailed/gb-nr:{self.station_code}/{check_date.strftime('%Y-%m-%d')}/0000-2359?stp=S&show=all"
            yield scrapy.Request(
                url=url, callback=self.parse, meta={"date": check_date}
            )

    def parse(self, response):
        services = response.css("a.service")

        for service in services:
            if self.is_potential_steam_train(service):

                time_str = service.css("div.time.plan.d::text").get(default="").strip()

                try:
                    # Parse date and time into datetime object in UTC
                    service_time = datetime.strptime(time_str, "%H%M").time()
                    dt_utc = datetime.combine(response.meta["date"], service_time)
                except ValueError as e:
                    dt_utc = None  # Fallback in case parsing fails

                yield {
                    "url": response.urljoin(service.attrib["href"]),
                    "station_code": self.station_code,
                    "headcode": service.css("div.tid::text").get(default="").strip(),
                    "origin": service.css("div.location.o span::text")
                    .get(default="")
                    .strip(),
                    "destination": service.css("div.location.d span::text")
                    .get(default="")
                    .strip(),
                    "scheduled_departure": dt_utc,
                    "platform": service.css("div.platform::text")
                    .get(default="")
                    .strip(),
                    "toc": service.css("div.toc::text").get(default="").strip(),
                }

    def is_potential_steam_train(self, train_data):
        stp_type = train_data.css("div.stp::text").get(default="").strip().upper()
        headcode = train_data.css("div.tid::text").get(default="").strip().upper()
        toc = train_data.css("div.toc::text").get(default="").strip().upper()

        return (
            stp_type == "STP" and HEADCODE_PATTERN.match(headcode) and toc in KNOWN_TOCS
        )

from datetime import datetime
import re

from .memory_db import ScheduleMemoryDB

class SteamWatchQuery:
    VALID_ATOC_CODES = {"WR", "LS", "TY"}
    HEADCODE_PATTERN = re.compile(r"[15]Z\d{2}")

    def __init__(self, db: ScheduleMemoryDB):
        self.db = db

    @property
    def now(self):
        return datetime.now()

    def get_stations(self):
        for date_s, services in self.db.by_date.items():
            date = datetime.strptime(date_s, "%Y-%m-%d")

            if date < self.now: # before now. I.e.: old services
                continue # next one
            
            for service in services:
                if service["CIF_stp_indicator"] != "N":
                    continue
                if service["atoc_code"] not in self.VALID_ATOC_CODES:
                    continue
                if not self.HEADCODE_PATTERN.match(service["schedule_segment"]["signalling_id"]):
                    continue

                stops = service["schedule_segment"]["schedule_location"]

                for stop in stops:
                    print(stop)
                    pass_time = stop.get("pass")
                    if not pass_time:
                        pass_time = stop.get("arrival")
                    if not pass_time:
                        pass_time = stop.get("departure")

                    # create new datetime object based on known date and pass/arrival time
                    # this does not account for trains running past midnight
                    dt = datetime(date.year, date.month, date.day, int(pass_time[:2]), int(pass_time[2:4]))
                    
                    yield {
                        "tiploc": stop["tiploc_code"],
                        "dt": dt,
                        "platform": stop["platform"]
                    }

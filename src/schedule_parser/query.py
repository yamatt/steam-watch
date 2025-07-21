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

    def all_stops(self):
        """
        The train doesn't stop at these stops, mostly. It just passes them.
        """
        for date_s, services in self.db.by_date.items():
            date = datetime.strptime(date_s, "%Y-%m-%d")

            if date < self.now: # skip if it's in the past
                continue
            
            for service in services:
                if service["CIF_stp_indicator"] != "N":
                    continue
                if service["atoc_code"] not in self.VALID_ATOC_CODES:
                    continue
                if not self.HEADCODE_PATTERN.match(service["schedule_segment"]["signalling_id"]):
                    continue

                stops = service["schedule_segment"]["schedule_location"]

                first_stop = stops[0]
                end_stop = stops[-1]

                for stop in stops:
                    pass_time = stop.get("pass") or stop.get("arrival") or stop.get("departure")

                    # create new datetime object based on known date and pass/arrival time
                    # this does not account for trains running past midnight
                    dt = datetime(date.year, date.month, date.day, int(pass_time[:2]), int(pass_time[2:4]))
                    
                    yield {
                        "atoc": service["atoc_code"],
                        "first_stop": {
                            "atoc": first_stop["tiploc_code"],
                        },
                        "end_stop": {
                            "atoc": end_stop["tiploc_code"],
                        },
                        "tiploc": stop["tiploc_code"],
                        "pass": dt,
                        "platform": stop["platform"],
                        "train_uid": service["CIF_train_uid"],
                        "signalling_id": service["schedule_segment"]["signalling_id"],
                        "stp": service["CIF_stp_indicator"]
                    }

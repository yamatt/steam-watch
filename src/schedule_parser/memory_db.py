from collections import OrderedDict
from functools import cached_property

from .collection import ScheduleCollection

class ScheduleMemoryDB:
    """
    A simple in-memory database for OpenRailData.
    This class is used to store and retrieve data related to OpenRailData.
    """

    def __init__(self, coll: ScheduleCollection):
        self.coll = coll
    
    @cached_property
    def schedule(self) -> list[dict]:
        db = OrderedDict()
        for item in self.coll.items:
            if "JsonScheduleV1" in item:
                schedule_item = item["JsonScheduleV1"]
                if schedule_item["transaction_type"] in ["Create", "Update"]:
                    db[(schedule_item["schedule_start_date"], schedule_item["CIF_train_uid"], schedule_item["CIF_stp_indicator"])] = schedule_item
                if schedule_item["transaction_type"] == "Delete":
                    db.pop((schedule_item["schedule_start_date"], schedule_item["CIF_train_uid"], schedule_item["CIF_stp_indicator"]), None)
        return db

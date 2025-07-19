from collections import OrderedDict
from functools import cached_property

from .parser import ScheduleParser

class ScheduleMemoryDB:
    """
    A simple in-memory database for OpenRailData.
    This class is used to store and retrieve data related to OpenRailData.
    """

    def __init__(self, parser: ScheduleParser):
        self.parser = parser

    @cached_property
    def tiplocs(self) -> dict[str, dict]:
        return dict([
            (tiploc["tiploc_code"], tiploc) for tiploc in self.parser.tiplocs if tiploc["transaction_type"] == "Create"
        ])
    
    @cached_property
    def schedule(self) -> list[dict]:
        return [
            item for item in self.parser.schedule_items if item["transaction_type"] == "Create"
        ]

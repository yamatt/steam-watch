from functools import cached_property
import json


class ScheduleParser:
    """
    Parse the SCHEDULE format from Open Rail Data
    """

    OPEN_AS = "r"
    BUFFER = 4096

    @classmethod
    def from_paths(cls, full_file_path: str, update_file_paths: list[str], encoding: str="utf-8") -> "ScheduleParser":
        """
        Create a ScheduleParser instance from a full file path and a list of update file paths.
        """

        return cls(
            full_file=open(full_file_path, cls.OPEN_AS, encoding=encoding, buffering=cls.BUFFER),
            update_files=[
                open(update_file_path, cls.OPEN_AS, encoding=encoding, buffering=cls.BUFFER) for update_file_path in update_file_paths
            ],
        )

    def __init__(self, full_file, update_files):
        """
        Initialize the ScheduleParser with a full file path and a list of update file paths.
        """
        self.full_file = full_file
        self.update_files = update_files

    @property
    def full(self):
        self.full_file.seek(0)
        return self.full_file

    @property
    def updates(self):
        return self.updates

    def get_entries(self, entry_type: str):
        return [
            entry[entry_type]
            for line in self.full
            if (entry := json.loads(line)) and entry_type in entry
        ]
        
    @cached_property
    def tiplocs(self):
        return self.get_entries("TiplocV1")

    @cached_property
    def schedule_items(self):
        return self.get_entries("JsonScheduleV1")

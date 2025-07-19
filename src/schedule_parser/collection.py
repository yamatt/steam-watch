from functools import cached_property
import json


class ScheduleCollection:
    """
    Parse the SCHEDULE format from Open Rail Data and manage as list
    """

    OPEN_AS = "r"
    BUFFER = 4096

    @classmethod
    def from_paths(cls, file_path_list: [str], encoding: str="utf-8") -> "ScheduleParser":
        """
        Create a ScheduleParser instance from a full file path and a list of update file paths.
        """
        return cls(
            files=[
                open(file_path, cls.OPEN_AS, encoding=encoding, buffering=cls.BUFFER) for file_path in file_path_list
            ]
        )

    def __init__(self, files=[]):
        """
        Initialize the ScheduleParser with a full file path and a list of update file paths.
        """
        self.files = files

    @cached_property
    def items(self):
        for file in self.files:
            with file as f:
                for line in f:
                    yield json.loads(line)

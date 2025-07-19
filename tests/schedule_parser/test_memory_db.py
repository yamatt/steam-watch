from unittest.mock import Mock, mock_open, patch

import pytest

from schedule_parser.memory_db import ScheduleMemoryDB
from schedule_parser.parser import ScheduleParser


class TestScheduleMemoryDB:
    def test_tiplocs(self):
        mock_schedule_parser = Mock(ScheduleParser)
        mock_schedule_parser.tiplocs = [
            {"tiploc_code": "ABC", "transaction_type": "Create", "name": "Station ABC"},
            {"tiploc_code": "XYZ", "transaction_type": "Delete", "name": "Station XYZ"},
        ]
        schedule_memory_db = ScheduleMemoryDB(mock_schedule_parser)

        results = schedule_memory_db.tiplocs

        assert len(results) == 1
        assert results["ABC"] == {
            "tiploc_code": "ABC",
            "transaction_type": "Create",
            "name": "Station ABC",
        }
        assert "XYZ" not in results

    def test_schedule(self):
        mock_schedule_parser = Mock(ScheduleParser)
        mock_schedule_parser.schedule_items = [
            {"transaction_type": "Create", "schedule_id": "S1"},
            {"transaction_type": "Update", "schedule_id": "S2"},
            {"transaction_type": "Create", "schedule_id": "S3"},
        ]
        schedule_memory_db = ScheduleMemoryDB(mock_schedule_parser)

        results = schedule_memory_db.schedule

        assert len(results) == 2
        assert results[0]["transaction_type"] == "Create"
        assert results[0]["schedule_id"] == "S1"
        assert results[1]["transaction_type"] == "Create"
        assert results[1]["schedule_id"] == "S3"

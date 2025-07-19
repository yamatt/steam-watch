from unittest.mock import Mock, mock_open, patch

import pytest

from schedule_parser.memory_db import ScheduleMemoryDB
from schedule_parser.collection import ScheduleCollection


class TestScheduleMemoryDB:
    def test_schedule(self):
        mock_schedule_parser = Mock(spec=ScheduleCollection)
        mock_schedule_parser.items = [
            {"JsonScheduleV1":{"CIF_stp_indicator":"N","CIF_train_uid":"example-1","schedule_start_date":"2025-07-14","transaction_type":"Create"}},
            {"JsonScheduleV1":{"CIF_stp_indicator":"N","CIF_train_uid":"example-2","schedule_start_date":"2025-07-14","transaction_type":"Delete"}},
        ]
        schedule_memory_db = ScheduleMemoryDB(mock_schedule_parser)

        results = schedule_memory_db.schedule

        assert len(results) == 1
        assert results[("2025-07-14", "example-1", "N")] == {
            "transaction_type": "Create",
            "schedule_start_date": "2025-07-14",
            "CIF_train_uid": "example-1",
            "CIF_stp_indicator": "N",
        }

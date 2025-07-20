from unittest.mock import Mock, mock_open, patch

import pytest

from schedule_parser.collection import ScheduleCollection
from schedule_parser.memory_db import ScheduleMemoryDB


@pytest.fixture
def mock_schedule_collection():
    mock_schedule_parser = Mock(spec=ScheduleCollection)
    mock_schedule_parser.items = [
        {
            "JsonScheduleV1": {
                "CIF_stp_indicator": "N",
                "CIF_train_uid": "example-1",
                "schedule_start_date": "2025-07-14",
                "transaction_type": "Create",
                "schedule_segment": {"signalling_id": "1Z40"},
            }
        },
        {
            "JsonScheduleV1": {
                "CIF_stp_indicator": "N",
                "CIF_train_uid": "example-2",
                "schedule_start_date": "2025-07-14",
                "transaction_type": "Delete",
                "schedule_segment": {"signalling_id": "1Z40"},
            }
        },
    ]
    return mock_schedule_parser


class TestScheduleMemoryDB:
    def test_services(self, mock_schedule_collection):

        schedule_memory_db = ScheduleMemoryDB(mock_schedule_collection)

        services = schedule_memory_db.services

        assert len(services) == 1
        assert ("2025-07-14", "example-1", "N") in services

    def test_by_date(self, mock_schedule_collection):

        schedule_memory_db = ScheduleMemoryDB(mock_schedule_collection)

        services = schedule_memory_db.by_date

        assert len(services) == 1
        assert "2025-07-14" in services

    def test_by_signal_id(self, mock_schedule_collection):

        schedule_memory_db = ScheduleMemoryDB(mock_schedule_collection)

        services = schedule_memory_db.by_signal_id

        assert len(services) == 1
        assert "1Z40" in services

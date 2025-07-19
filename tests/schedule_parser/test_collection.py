from unittest.mock import mock_open, patch

import pytest

from schedule_parser.collection import ScheduleCollection


@pytest.fixture
def mock_schedule_collection():
    with patch(
        "builtins.open",
        mock_open(read_data='{"TiplocV1": {"code": "ABC", "name": "Station ABC"}}'),
    ) as mock_file:
        yield ScheduleCollection(files=[mock_file()])


class TestParser:
    def test_iter(self, mock_schedule_collection):
        items = list(mock_schedule_collection.items)
        assert len(items) == 1
        assert items == [{"TiplocV1": {"code": "ABC", "name": "Station ABC"}}]

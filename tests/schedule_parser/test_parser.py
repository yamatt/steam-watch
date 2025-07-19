from unittest.mock import mock_open, patch

import pytest

from schedule_parser.parser import ScheduleParser


@pytest.fixture
def mock_schedule_parser():
    with patch(
        "builtins.open",
        mock_open(read_data='{"TiplocV1": {"code": "ABC", "name": "Station ABC"}}'),
    ) as mock_file:
        yield ScheduleParser(full_file=mock_file(), update_files=[])


class TestParser:
    def test_get_entries(self, mock_schedule_parser):
        results = mock_schedule_parser.get_entries("TiplocV1")

        assert len(results) == 1
        assert results[0] == {"code": "ABC", "name": "Station ABC"}

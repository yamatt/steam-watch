import json

from email_render.render import render


def test_render(tmp_path):
    message_file = tmp_path / "message.txt"
    message_file.write_text("This is a test message.")

    tiploc = "TESTLOC"
    result = render(tiploc, str(message_file))

    expected_output = {
        "subject": "Possible steam trains found",
        "body": "This is a test message.",
        "tags": ["steam", tiploc],
    }

    assert json.loads(result) == expected_output

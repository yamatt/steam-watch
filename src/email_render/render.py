import json

EMAIL_JSON = {
    "subject": "Possible steam trains found",
    "body": "Possible steam train found",
    "tags": ["steam"],
}

def render(tiploc, message_file_path):
    data = EMAIL_JSON.copy()
    with open(message_file_path) as f:
        data["body"] = f.read()
        data["tags"].append(tiploc)

    return json.dumps(data)

import json

DM_JSON = {
    "msgtype":"m.text",
    "body": None
}

def render(message_file_path):
    data = DM_JSON.copy()
    with open(message_file_path) as f:
        data["body"] = f.read()

    return json.dumps(data)

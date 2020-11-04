import json


def jsonify(data):
    response_body = json.dumps(data).encode("utf-8")

    headers = [("Content-Type", "application/json"), ("Content-Length", str(len(response_body)))]
    return response_body, headers

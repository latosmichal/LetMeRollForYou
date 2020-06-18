import json

import requests


def get_roll_from_random(k=6):
    req = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": "",
            "n": 2,
            "min": 1,
            "max": k,
            "replacement": True
        },
        "id": 42
    }
    json_req = json.dumps(req)

    headers = {
        'Content-type': 'application/json',
    }

    r = requests.post(
        'https://api.random.org/json-rpc/2/invoke', 
        headers=headers,
        data=json_req
        )
    j = r.json()

    return j['result']['random']['data']
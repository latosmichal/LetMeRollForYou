import json

import requests


def get_roll_from_random(k=6, n=1):
    req = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": "ed4f8294-a9d9-431b-9bd8-233e086753fb",
            "n": n,
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
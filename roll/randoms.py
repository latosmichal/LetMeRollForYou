import json

import requests


def get_roll_from_random(k=6, n=1):
    req = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": "",
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

    response = requests.post(
        'https://api.random.org/json-rpc/2/invoke', 
        headers=headers,
        data=json_req
        )
    json_response = response.json()

    try:
        result = json_response['result']['random']['data']
    except KeyError:
        message = json_response['error']['message']
        raise ResourceWarning(message)
        result = None

    return result
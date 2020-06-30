import json

import requests
import os
random_token = os.getenv('RANDOM_TOKEN')

def get_roll_from_random(k=6, n=1):
    req = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": random_token,
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
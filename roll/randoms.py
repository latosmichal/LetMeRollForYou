import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

random_token = os.getenv('RANDOM_TOKEN')

def get_roll_from_random(k=6, n=1):
    if int(k)==1:
        return [1]*n

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
        raise ResourceWarning('API error: {}'.format(message))
        result = None

    return result
import requests
import json

def send_viber_message(message):
    METBOTV_API_TOKEN = '4ca366e7cec00c05-71d303c1932c9df5-409d3fc23db8f30'
    LENA_API_TOKEN = '4cc512f93a67d2c0-1712a832c410d948-471a0d759e4d88ec'
    headers = {
        'X-Viber-Auth-Token': LENA_API_TOKEN,
    }
    url = 'https://chatapi.viber.com/pa/send_message'
    data = {
        "receiver":"+EdDG1RrsZXcbC3bfUoz/w==",
        "min_api_version":1,
        "sender": {
            "name":"lena photo bot"
        },
        "type":"text",
        "text": message,
    }
    response = requests.post(url, data = json.dumps(data), headers=headers)
import requests
import json
from server import DATABASE_NAME

sample_post = {
    "userId": "ABC123XYZ",
    "sessionId": "XYZ456ABC",
    "actions": [
        {
            "time": "2018-10-18T21:37:28-06:00",
            "type": "CLICK",
            "properties": {
                "locationX": 52,
                "locationY": 11
            }
        },
        {
            "time": "2018-10-18T21:37:30-06:00",
            "type": "VIEW",
            "properties": {
                "viewedId": "FDJKLHSLD"
            }
        },
        {
            "time": "2018-10-18T21:37:30-06:00",
            "type": "NAVIGATE",
            "properties": {
                "pageFrom": "communities",
                "pageTo": "inventory"
            }
        }
    ]
}

r = requests.post('http://localhost:5000/add-log', json=json.dumps(sample_post))
assert (r.json()['message'] == 'added log to database')

NUMBER_OF_USERS = 100
for i in range(0, NUMBER_OF_USERS):
    sample_post['userId'] = str(i)
    r = requests.post('http://localhost:5000/add-log', json=json.dumps(sample_post))
    assert (r.json()['message'] == 'added log to database')


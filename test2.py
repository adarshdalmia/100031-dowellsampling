
import requests
import json
def dowellConnection(data):
    url = "http://100002.pythonanywhere.com/"
    command = data['command']
    field = data['field']
    update_field = data['update_field']
    payload = json.dumps({
    "cluster": "license",
    "database": "license",
    "collection": "licenses",
    "document": "licenses",
    "team_member_ID": "689044433",
    "function_ID": "ABCDE",
    "command": "fetch",
    "field": {},
    "update_field": None,
    "platform": "bangalore"
})
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

print(dowellConnection({"command": "fetch", "field": {}, "update_field": None}))
import requests
import json

def dowellConnection(data):
    url = "http://100002.pythonanywhere.com/"
    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.json()

def dowell_purposive_sampling(search_criteria):
    n = 10

    sample_values = []
    data = {
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
    }
    response = dowellConnection(data)
    all_data = response.get("data", [])

    for item in all_data:
        # check if item matches the search criteria
        if all(item.get(key) == value for key, value in search_criteria):
            sample_values.append(item)
            if len(sample_values) == n:
                break

    return sample_values

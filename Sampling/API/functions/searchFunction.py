import requests
import json

def dowellConnection(data):
    url = "http://100002.pythonanywhere.com/"
    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    print(response)
    return response.json()

def dowell_purposive_sampling(search_criteria, user_field, manual_data):
    n = 1000000
    sample_values = []
    data = {
        "cluster": user_field.get("cluster", ""),
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

    if manual_data:
        all_data = manual_data.get("data", [])
    else:
        response = dowellConnection(data)
        all_data = response.get("data", [])

    for item in all_data:
        # check if all search criteria values are present in the corresponding item's values
        criteria_satisfied = True
        for key, value in search_criteria:
            if key not in item or value not in str(item[key]):
                criteria_satisfied = False
                break
        if criteria_satisfied:
            sample_values.append(item)
            if len(sample_values) == n:
                break

    return sample_values

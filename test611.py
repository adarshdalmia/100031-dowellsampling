import requests
import json
from sample_size import dowell_sample_size

def dowellConnection(data):
    url = "http://100002.pythonanywhere.com/"
    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

def dowell_purposive_sampling():
    n= 4
    search_count = int(input("Enter the number of data you want to search: "))
    fields_count = int(input("Enter the number of fields you want to select: "))

    search_criteria = []
    for i in range(search_count):
        key = input("Enter the key for search criteria: ")
        value = input("Enter the value for search criteria: ")
        search_criteria.append((key, value))

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

if __name__ == "__main__":
    print(dowell_purposive_sampling())
{
    "cluster": "license",
    "database": "license",
    "collection": "licenses",
    "document": "licenses",
    "team_member_ID": "689044433",
    "function_ID": "ABCDE",
    "platform": "bangalore"
}
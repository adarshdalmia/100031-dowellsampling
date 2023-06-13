import requests
import json
def dowellConnection(data):
    url = "http://100002.pythonanywhere.com/"
    command = data['command']
    field = data['field']
    update_field = data['update_field']
    payload = json.dumps({
        "cluster": "dowellfunctions",
        "database": "dowellfunctions",
        "collection": "classification",
        "document": "classification",
        "team_member_ID": "1196001",
        "function_ID": "ABCDE",
        "command": 'fetch',
        "field": {},
        "update_field": None,
        "platform": "bangalore"
        })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

# print(dowellConnection({'command': 'fetch', 'field': {}, 'update_field': None}))

data = [
    {
        '_id': '64883171580f89d9f06b2bec',
        'allBaskets': {
            'country': [
                {'item': 'India', 'itemLink': 'Asia'},
                {'item': 'USA', 'itemLink': 'North America'},
                {'item': 'Germany', 'itemLink': 'Europe'}
            ],
            'state': [
                {'item': 'Uttar Pradesh', 'itemLink': 'India'},
                {'item': 'Maharashtra', 'itemLink': 'India'},
                {'item': 'Georgia', 'itemLink': 'USA'},
                {'item': 'Nevada', 'itemLink': 'USA'},
                {'item': 'Bavaria', 'itemLink': 'Germany'},
                {'item': 'Brandenburg', 'itemLink': 'Germany'}
            ],
            'city': [
                {'item': 'Agra', 'itemLink': 'Uttar Pradesh'},
                {'item': 'Noida', 'itemLink': 'Uttar Pradesh'},
                {'item': 'Pune', 'itemLink': 'Maharashtra'},
                {'item': 'Mumbai', 'itemLink': 'Maharashtra'},
                {'item': 'Atlanta', 'itemLink': 'Georgia'},
                {'item': 'Carson City', 'itemLink': 'Nevada'},
                {'item': 'Munich', 'itemLink': 'Bavaria'},
                {'item': 'Potsdam', 'itemLink': 'Brandenburg'}
            ]
        },
        'basketOrder': []
    },
    {
        '_id': '64883183580f89d9f06b2bf6',
        'classificationType': 'N',
        'numberOfLevels': 3,
        'eventId': 'FB1010000000000000000000003004',
        'permutationsVariables': [],
        'dbInsertedId': '64883171580f89d9f06b2bec',
        'baskets': ['country', 'state', 'city']
    },
    {
        '_id': '6488319a580f89d9f06b2c02',
        'allBaskets': {
            'country': [
                {'item': 'India', 'itemLink': 'Asia'},
                {'item': 'USA', 'itemLink': 'North America'},
                {'item': 'Germany', 'itemLink': 'Europe'}
            ],
            'state': [
                {'item': 'Uttar Pradesh', 'itemLink': 'India'},
                {'item': 'Maharashtra', 'itemLink': 'India'},
                {'item': 'Georgia', 'itemLink': 'USA'},
                {'item': 'Nevada', 'itemLink': 'USA'},
                {'item': 'Bavaria', 'itemLink': 'Germany'},
                {'item': 'Brandenburg', 'itemLink': 'Germany'}
            ],
            'city': [
                {'item': 'Agra', 'itemLink': 'Uttar Pradesh'},
                {'item': 'Noida', 'itemLink': 'Uttar Pradesh'},
                {'item': 'Pune', 'itemLink': 'Maharashtra'},
                {'item': 'Mumbai', 'itemLink': 'Maharashtra'},
                {'item': 'Atlanta', 'itemLink': 'Georgia'},
                {'item': 'Carson City', 'itemLink': 'Nevada'},
                {'item': 'Munich', 'itemLink': 'Bavaria'},
                {'item': 'Potsdam', 'itemLink': 'Brandenburg'}
            ]
        },
        'basketOrder': []
    }
]
data = dowellConnection({'command': 'fetch', 'field': {}, 'update_field': None})
desired_data = []

for item in data:
    if 'allBaskets' in item and 'basketOrder' in item:
        all_baskets = item['allBaskets']
        basket_order = item['basketOrder']
        basket_data = []

        for basket in basket_order:
            basket_items = all_baskets.get(basket, [])
            basket_data.append({basket: basket_items})

        desired_data.append(basket_data)

print(desired_data)
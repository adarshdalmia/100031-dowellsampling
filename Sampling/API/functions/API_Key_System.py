import requests

# def processApikey(api_key, api_service):
#     url = 'https://100105.pythonanywhere.com/api/v1/process-api-key/'
#     payload = {
#         "api_key" : api_key,
#         "api_service_id" : api_service
#     }
#     response = requests.post(url, json=payload)
#     return response.text


def processApikey(api_key):
    url = f'https://100105.pythonanywhere.com/api/v3/process-services/?type=api_service&api_key={api_key}'
    payload = {
        "service_id": "DOWELL10011"
    }

    response = requests.post(url, json=payload)
    return response.text
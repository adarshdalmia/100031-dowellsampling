import requests

def processApikey(api_key, api_service):
    url = 'https://100105.pythonanywhere.com/api/v1/process-api-key/'
    payload = {
        "api_key" : api_key,
        "api_service_id" : api_service
    }
    response = requests.post(url, json=payload)
    return response.text
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
import requests
from API.functions.stratifiedSampling import dowellStratifiedSampling
from API.functions.sampleSize import dowellSampleSize
from API.functions.systematic_sampling import dowellSystematicSampling
from API.functions.simpleRandomSampling import dowellSimpleRandomSampling


@csrf_exempt
def get_data(request):
    data = {
        "finalOutput": [
            ["India", "Germany"],
            ["Uttar Pradesh", "Georgia"],
            ["Pune", "Munich"],
            ["Mumbai", "Berlin"],
            ["Delhi", "Hamburg"],
            ["Kolkata", "Hamburg"],
            ["MP", "Hamburg"],
        ]
    }
    return JsonResponse(data)

def get_YI_data():
    api_url = 'http://localhost:8000/API/get_data/'
    response = requests.get(api_url)
    if response.status_code == 200:
        json_data = response.json()
        data = json_data['finalOutput']
    return data

def stratified_sampling(request):
    # Get input parameters from POST request
    Yi = get_YI_data()
    stratifiedSamplingInput = {
    'e': 0.1,
    'allocationType': 'proportional',
    'samplingType': 'geometricalApproach',
    'insertedId': 'some_id',
    'replacement': True,
    'Yi': Yi,
    }
    result = dowellStratifiedSampling(stratifiedSamplingInput)
    return JsonResponse(result)

def systematic_sampling(request):
    Yi = get_YI_data()
    samples = dowellSystematicSampling(Yi)
    response = {
            'samples': samples
        }
    return JsonResponse(response)

def simple_random_sampling(request):
    Yi = get_YI_data()
    e = 0.05 # desired margin of error (5%)
    N = len(Yi)
    n = dowellSampleSize(N, e)
    method = 'geometricalApproach'
    samples = dowellSimpleRandomSampling(n,N,Yi,method)
    response = samples
    return JsonResponse(response)
'''
Types of sampling
1. Stratified Random Sampling
Request
{

}

Response
{

}

2. Systematic Sampling
Request
{

}

Response
{

}

3. Purposive Sampling
Request
{

}

Response
{

}

4. Cluster
Request
{

}

Response
{

}

'''
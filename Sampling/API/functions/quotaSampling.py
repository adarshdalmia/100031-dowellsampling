from sampleSize import dowellSampleSize
from purposiveSampling import dowellPurposiveSampling
import time


# def quota_sampling(population_units, population_size):
import requests
import json

insertedId = input("Enter InsertID:")


def populationUnits(insertedId):

    url = "http://100061.pythonanywhere.com/api/"

    payload = json.dumps({
        "inserted_id": insertedId,
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload).json()
    Yi = response['classifiedData']

    return Yi


def quota_sampling(population_units, population_size, unit):
    # population_units = eval(input("Enter population unit: "))
    # population_size = int(input("Enter population size: "))
    process_time = 0
    n = dowellSampleSize(population_units, margin_of_error=0.05)
    quotas = []
    sample_units = []
    purposive_input = {}
    Yi = population_units
    all_quotas = {}
    ni = {}
    N = population_size

    for i in range(len(Yi.get(0))):
        quotas.append(i)
    k = len(quotas)

    for i in quotas:
        tempList = []
        for j in range(len(Yi)):
            print(j)
            tempList.append(Yi.get(j).get(i))
        all_quotas[i] = tempList

    if isinstance(n, int):
        for i in range(1, k+1):
            Ni = len(all_quotas[quotas[i-1]])
            ni[quotas[i-1]] = dowellSampleSize(N, n, Ni)
            purposive_input["N"] = N
            purposive_input["e"] = 0.05
            purposive_input["Yi"] = Yi
            purposive_input["unit"] = unit
            sample = dowellPurposiveSampling(purposive_input)
            sample_units.append(sample)

    process_time = time.process_time()

    print(sample_units, process_time)

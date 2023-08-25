from API.functions.stratifiedSampling import populationUnits
from randomGeneration import dowellRandomGeneration
from sampleSize import dowellSampleSize
import time
import requests
import json


def pps_sampling(population_size, size, insertId):
    Yi = populationUnits(insertId)
    N = population_size
    n = dowellSampleSize(N, margin_of_error=0.05)
    Si = size
    sample = 0

    if len(Yi) < 5:
        return "Please try another sample method"

    rand1, rand2 = dowellRandomGeneration(
        N, n, Yi), dowellRandomGeneration(N, n, Yi)

    if not (1 <= rand1[0] <= N) and not (1 <= rand2[0] <= Si):
        return "The selected random numbers are not appropriate"

    while sample != n:
        if rand2[0] <= Si:
            sample = Yi[rand1[0]]
        else:
            pass

    process_time = time.process_time()
    return sample, process_time
import json
import math
import time
from django.http import JsonResponse, HttpResponse


def dowellSampleSize(N, e , cl=0.99, sd=None):
    try:
        population_size = N
        error = e
        confidence_level = cl
        standard_deviation =sd

        if population_size is not None:
            population_size = int(population_size)
            if population_size <= 0 or error <= 0:
                return JsonResponse({'error': 'Invalid input. Population size and error must be positive.'}, status=400)
            if standard_deviation is not None:
                standard_deviation = float(standard_deviation)
                sample_size, process_time, method_used = calculate_sample_size_with_known_sd(population_size, error, confidence_level, standard_deviation)
            else:
                sample_size, process_time, method_used = calculate_sample_size_using_slovin(population_size, error)

        else:
            if standard_deviation is not None:
                standard_deviation = float(standard_deviation)
                sample_size, process_time, method_used = calculate_sample_size_without_pop_size(error, confidence_level, standard_deviation)
            else:
                sample_size, process_time, method_used = calculate_sample_size_using_slovin(population_size, error)

        return sample_size

    except Exception as e:
        return e

def calculate_sample_size_with_known_sd(population_size, error, confidence_level, standard_deviation):
    process_time = 0
    z = get_z_score(confidence_level)
    p = 0.5 
    q = 1 - p
    numerator = (z ** 2) * p * q
    denominator = (error ** 2) * (1 + (((z ** 2) * p * q) / (error ** 2 * population_size)))
    sample_size = numerator / denominator
    process_time = time.process_time()
    method_used = 'finite_population'
    return sample_size, process_time, method_used

def calculate_sample_size_using_slovin(population_size, error):
    process_time = 0
    sample_size = population_size / (1 + population_size * error ** 2)
    sample_size_rounded = math.ceil(sample_size)
    process_time = time.process_time()
    method_used = 'slovin'
    if 1 < sample_size_rounded < 500:
        return sample_size_rounded , process_time, method_used
    else:
        return "Sample size is not adequate", process_time, method_used

def calculate_sample_size_without_pop_size(error, confidence_level, standard_deviation):
    process_time = 0
    z = get_z_score(confidence_level)
    p = 0.5 
    sample_size = (z ** 2 * p * (1 - p)) / (error ** 2)
    process_time = time.process_time()
    method_used = 'infinite_population'
    return sample_size , process_time, method_used

def get_z_score(confidence_level):
    if confidence_level == 0.90:
        return 1.645
    elif confidence_level == 0.95:
        return 1.96
    elif confidence_level == 0.99:
        return 2.58
    else:
        raise ValueError("Invalid confidence level. Supported values: 0.90, 0.95, 0.99")



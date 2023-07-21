import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from django.views.decorators.csrf import csrf_exempt
import math
from urllib.parse import urlparse, parse_qs

@csrf_exempt
def calculate_sample_size(request,population):
    print(population)
    try:
        data = json.loads(request.body)
        population_size = int(data.get('population_size', 0))
        margin_of_error = float(data.get('margin_of_error', 0))
        print(population_size)
        print(margin_of_error)
        if population_size <= 0 or margin_of_error <= 0:
            return JsonResponse({'error': 'Invalid input. Population size and margin of error must be positive.'}, status=400)

        try:
            confidence_level = float(data.get('confidence_level', 0.99))
        except ValueError:
            return JsonResponse({'error': 'Invalid confidence level. Supported values: 0.90, 0.95, 0.99'}, status=400)

        sample_size = dowellSampleSize(population_size, margin_of_error, population, confidence_level)
        return JsonResponse({'sample_size': sample_size})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def dowellSampleSize(population_size, margin_of_error, population, confidence_level):
    z = 0.0
    if confidence_level == 0.90:
        z = 1.645
    elif confidence_level == 0.95:
        z = 1.96
    elif confidence_level == 0.99:
        z = 2.576
    else:
        raise ValueError("Invalid confidence level. Supported values: 0.90, 0.95, 0.99")

    if population == "finite":
        p = 0.5  # Assuming worst-case scenario where p = 0.5
        q = 1 - p
        e = margin_of_error

        numerator = (z ** 2) * p * q
        denominator = (e ** 2) * (1 + (((z ** 2) * p * q) / (e ** 2 * population_size)))

        sample_size = numerator / denominator
        sample_size_rounded = math.ceil(sample_size)
    elif population == "infinite":
        p = 0.5  # Assuming worst-case scenario where p = 0.5
        e = margin_of_error
        q = 1 - p
        sample_size = (z ** 2 * p * q) / (e ** 2)
        sample_size_rounded = math.ceil(sample_size)
    elif population == "slovins":
        e = margin_of_error
        sample_size = population_size / (1 + population_size * e * e)
        sample_size_rounded = math.ceil(sample_size)
        if sample_size_rounded > 1 and sample_size_rounded < 500:
            return sample_size_rounded
        else:
            return "Sample size is not adequate"
    else:
        raise ValueError("Invalid population type. Supported values: 'finite', 'infinite', 'slovins'")
    
    return sample_size_rounded

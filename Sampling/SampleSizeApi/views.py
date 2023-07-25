import json
import math
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def calculate_sample_size(request):
    try:
        data = json.loads(request.body)
        population_size = data.get('population_size')
        error = float(data.get('error', 0))
        confidence_level = float(data.get('confidence_level', 0.95))
        standard_deviation = data.get('standard_deviation')

        if population_size is not None:
            population_size = int(population_size)
            if population_size <= 0 or error <= 0:
                return JsonResponse({'error': 'Invalid input. Population size and error must be positive.'}, status=400)
            if standard_deviation is not None:
                standard_deviation = float(standard_deviation)
                sample_size = calculate_sample_size_with_known_sd(population_size, error, confidence_level, standard_deviation)
            else:
                sample_size = calculate_sample_size_using_slovin(population_size, error)
        else:
            if standard_deviation is not None:
                standard_deviation = float(standard_deviation)
                sample_size = calculate_sample_size_without_pop_size(error,confidence_level, standard_deviation)
            else:
                sample_size = calculate_sample_size_using_slovin(population_size, error)

        return JsonResponse({'sample_size': sample_size})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def calculate_sample_size_with_known_sd(population_size, error, confidence_level, standard_deviation):
    z = get_z_score(confidence_level)
    p = 0.5 
    q = 1 - p

    numerator = (z ** 2) * p * q
    denominator = (error ** 2) * (1 + (((z ** 2) * p * q) / (error ** 2 * population_size)))

    sample_size = numerator / denominator
    return math.ceil(sample_size)

def calculate_sample_size_using_slovin(population_size, error):
    sample_size = population_size / (1 + population_size * error ** 2)
    sample_size_rounded = math.ceil(sample_size)
    if 1 < sample_size_rounded < 500:
        return sample_size_rounded
    else:
        return "Sample size is not adequate"

def calculate_sample_size_without_pop_size(error, confidence_level, standard_deviation):
    z = get_z_score(confidence_level)
    p = 0.5  # Assuming worst-case scenario where p = 0.5

    sample_size = (z ** 2 * p * (1 - p)) / (error ** 2)
    return math.ceil(sample_size)



def get_z_score(confidence_level):
    if confidence_level == 0.90:
        return 1.645
    elif confidence_level == 0.95:
        return 1.96
    elif confidence_level == 0.99:
        return 2.576
    else:
        raise ValueError("Invalid confidence level. Supported values: 0.90, 0.95, 0.99")

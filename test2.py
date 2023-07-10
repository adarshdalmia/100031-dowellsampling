import math

def calculate_sample_size(population_size, confidence_level, margin_of_error, finite_population=False):
    z = 0.0
    if confidence_level == 0.90:
        z = 1.645
    elif confidence_level == 0.95:
        z = 1.96
    elif confidence_level == 0.99:
        z = 2.576
    else:
        raise ValueError("Invalid confidence level. Supported values: 0.90, 0.95, 0.99")
    if finite_population:
        p = 0.5  # Assuming worst-case scenario where p = 0.5
        q = 1 - p
        e = margin_of_error

        numerator = (z ** 2) * p * q
        denominator = (e ** 2) * (1 + (((z ** 2) * p * q) / (e ** 2 * population_size)))

        sample_size = numerator / denominator
        sample_size_rounded = math.ceil(sample_size)
    else:
        p = 0.5  # Assuming worst-case scenario where p = 0.5
        e = margin_of_error
        q = 1 - p
        sample_size = (z ** 2 * p * q) / (e ** 2)
        sample_size_rounded = math.ceil(sample_size)

    return sample_size_rounded


# Finite population example
population_size = 400
confidence_level = 0.99
margin_of_error = 0.05

sample_size = calculate_sample_size(population_size, confidence_level, margin_of_error, finite_population=True)
print(f"The required sample size for a finite population is: {sample_size}")

# Infinite population example
population_size = 10000
confidence_level = 0.99
margin_of_error = 0.05

sample_size = calculate_sample_size(population_size, confidence_level, margin_of_error)
print(f"The required sample size for an infinite population is: {sample_size}")

# Step 1: Choose a representative dataset
import random
from Sampling.API.functions.systematic_sampling import dowellSystematicSampling


test_dataset = [
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J"
]

# Step 2: Define the input
test_input = {
    "population": test_dataset,
    "population_size": len(test_dataset)
}

# Step 3: Run the function
sample_units = dowellSystematicSampling(test_input)

# Step 4: Manually perform systematic sampling
n = 3  # Sample size
k = len(test_dataset) // n  # Number of groups
start_position = random.randint(0, k - 1)
expected_sample_units = [test_dataset[start_position + j * k] for j in range(n)]

# Step 5: Compare results
if sample_units == expected_sample_units:
    print("Function works correctly!")
else:
    print("Function does not produce expected results.")
    print("Expected:", expected_sample_units)
    print("Actual:", sample_units)

import random
import time

# Function to generate random numbers for i and j
def dowell_random_generation(N, M):
    i = random.randint(1, N)
    j = random.randint(1, M)
    return i, j

# Function to calculate Dowell sample size
def dowell_sample_size(N):
    return int(0.05 * N)  # You can adjust the sampling rate as needed

# Function to perform PPS sampling using Lahiri method
def pps_sampling_lahiri(Population_units, Population_size, sample_size, size):
    # Initialize the selected units list and process start time
    selected_units = []
    start_time = time.time()

    while len(selected_units) < sample_size:
        i, j = dowell_random_generation(Population_size, size)

        if 1 <= i <= Population_size and 1 <= j <= size:
            Si = Population_units[j - 1]  # Assuming index is 0-based
            if j <= Si:
                selected_units.append(i)
        else:
            print("Selected random numbers are not appropriate")

    # Calculate process time
    process_time = time.time() - start_time

    return selected_units, process_time

# Example values
Population_units = [5, 3, 7, 2, 6, 4, 8, 1]  # Replace with your population units
Population_size = len(Population_units)
sample_size = dowell_sample_size(Population_size)
size = max(Population_units)

# Call the PPS sampling function
sample_units, process_time = pps_sampling_lahiri(Population_units, Population_size, sample_size, size)

print("Selected sample units:", sample_units)
print("Process time:", process_time, "seconds")

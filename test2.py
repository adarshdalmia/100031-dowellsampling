import random

def dowellsnowballsampling(population_units, population_size, sample_size, reference):
    sample_units = []
    process_time = 0
    
    # Function to calculate the sample size using Dowell's formula
    def dowellsamplesize():
        return int((population_size * sample_size) / (population_size + sample_size - 1))

    # Function to find a random unit from the population
    def select_random_unit():
        return random.choice(population_units)

    # Function to find a connection/reference for a given unit
    def find_connection(unit):
        while True:
            connection = input(f"Find a connection/reference for unit '{unit}': ")
            if connection == reference:
                print("Reference cannot be the same as the original unit.")
            else:
                return connection

    # Ask user to select the first unit to be included in the sample
    first_unit = input("Select the first unit to include in the sample: ")
    sample_units.append(first_unit)
    process_time += 1

    # Loop to select subsequent units using Dowell's Snowball Sampling method
    while len(sample_units) < sample_size:
        current_unit = select_random_unit()
        process_time += 1

        # Find a connection/reference for the current unit
        connection = find_connection(current_unit)
        process_time += 1

        # Check if the connection is not already in the sample
        if connection not in sample_units:
            sample_units.append(connection)
        else:
            print("Selected connection already exists in the sample. Select another connection.")

    return sample_units, process_time

# Example usage
if __name__ == "__main__":
    population_units = ["insta profile", "same post", "refer another", "different post"]
    population_size = len(population_units)
    
    sample_size = int(input("Enter the desired sample size: "))
    reference = input("Enter the reference to a particular thing: ")

    result, time_taken = dowellsnowballsampling(population_units, population_size, sample_size, reference)
    print("Sample Units:", result)
    print("Process Time:", time_taken)

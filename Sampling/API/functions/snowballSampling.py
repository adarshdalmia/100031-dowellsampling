import time


def dowellsnowballsampling(Yi, N, n, Ri):
    sample_units = []
    process_time = 0
    print("Select the first unit to be included in the sample:")
    unit_1 = input()
    sample_units.append(unit_1)
    print(f"Find a connection/reference from {unit_1} to select the second unit in the sample:")
    R1 = input()
    for i in range(2, n+1):
        print(f"Select the {i}th unit to be included in the sample:")
        unit_i = input()

        valid_connection = False
        while not valid_connection:
            print(f"Find a connection/reference from {unit_i} (excluding {R1}) for the {i}th unit:")
            Ri = input()

            if Ri == R1:
                print("Select another connection. It should not be the same as the previous connection.")
            else:
                valid_connection = True

        sample_units.append(unit_i)

    # Calculate the process time
    process_time = time.process_time()

    return sample_units, process_time

def main():
    Yi = input("Enter the population units: ")
    N = int(input("Enter the population size: "))
    n = int(input("Enter the sample size: "))
    Ri = input("Enter the reference: ")

    sample_units, process_time = dowellsnowballsampling(Yi, N, n, Ri)

    print("\nSample units:",sample_units)

    print(f"\nProcess time: {process_time} seconds")


if __name__ == "__main__":
    main()
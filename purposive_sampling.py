from sample_size import dowell_sample_size


def dowell_purposive_sampling():
    n, N = dowell_sample_size()
    Yi_input = input("Enter the population values(space separated): ")
    Yi = [int(i) for i in Yi_input.split()]

    sample_values = []
    for _ in range(n):
        unit = int(input("Select the units to be included in the sample: "))
        if unit in N:
            sample_values.append(unit)
        else:
            unit = input("Select another available unit")

    return sample_values


if __name__ == "__main__":
    print(dowell_purposive_sampling())

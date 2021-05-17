from sample_size import dowell_sample_size


def dowell_purposive_sampling():
    n, N = dowell_sample_size()
    Yi_input = input("Enter the population values(comma separated): ")
    # assumes values are integers
    Yi = [int(i) for i in Yi_input.split(",")]

    sample_values = []
    while len(sample_values) < n:
        units_inp = input("Enter the population values(comma separated): ")
        # assumes values are integers
        units = [int(i) for i in units_inp.split(",")]

        # check if selected units are matching with the population units
        for i in units:
            if i not in Yi:
                print("Select another available unit")
                break
        else:
            sample_values.append(units)

    return sample_values


if __name__ == "__main__":
    print(dowell_purposive_sampling())

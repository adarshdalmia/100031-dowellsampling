from sample_size import dowell_sample_size
from geometrical_approach import dowell_geometrical_function
from random_generation import dowell_random_generation
from mechanical_randomisation import dowell_random_table
from statistics import pvariance
from random import shuffle


def dowell_random_sampling():
    n, N = dowell_sample_size()
    Yi_input = input("Enter the population values(comma separated): ")
    # assumes values are integers
    Yi = [int(i) for i in Yi_input.split(",")]

    variance = pvariance(Yi)
    # variance too low
    if variance > 1:
        print("simple random sampling can not be used")

    while True:
        method = input(
            """
Select either 1, 2 or 3

Location based:
    Geometric Approach(Enter 1)
Number/Value based:
    Mechanical Randomisation(Enter 2)
    Random Number Generation(Enter 3)
"""
        )
        if method in ["1", "2", "3"]:
            break
        else:
            print(f"{method} is not one of the options.")

    # shuffle Population units
    shuffle(Yi)

    func_dict = {
        "1": dowell_geometrical_function,
        "2": dowell_random_table,
        "3": dowell_random_generation,
    }
    kwargs = {"n": n, "N": N, "Yi": Yi}
    sample_units = func_dict[method](**kwargs)

    return sample_units


if __name__ == "__main__":
    print(dowell_random_sampling())

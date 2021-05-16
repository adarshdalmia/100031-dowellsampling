from sample_size import dowell_sample_size
from geometrical_approach import dowell_geometrical_function
from random_generation import dowell_random_generation
from mechanical_randomisation import dowell_random_table
from statistics import pvariance
from random import shuffle


def dowell_random_sampling():
    n, N = dowell_sample_size()
    Yi_input = input("Enter the population values(space separated): ")
    Yi = [int(i) for i in Yi_input.split()]

    variance = pvariance(Yi)
    # variance too low
    if variance > 1:
        print("simple random sampling can not be used")

    start = int(input("Enter the initial point: "))
    method = input(
        """
Select either 1, 2, 3 or 4

Location based:
    Random Graph(Enter 1)
    Geometric Approach(Enter 2)
Number/Value based:
    Mechanical Randomisation(Enter 3)
    Random Number Generation(Enter 4)
"""
    )

    # shuffle Population units
    shuffle(Yi)

    func_dict = {
        "1": dowell_random_graph,
        "2": dowell_geometrical_function,
        "3": dowell_random_table,
        "4": dowell_random_generation,
    }
    kwargs = {"n": n, "N": N, "Yi": Yi}
    sample_units = func_dict[method](**kwargs)

    return sample_units


if __name__ == "__main__":
    dowell_random_sampling()

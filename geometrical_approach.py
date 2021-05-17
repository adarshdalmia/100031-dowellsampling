from random import randrange
from sample_size import dowell_sample_size


def dowell_geometrical_function(N=None, n=None, Yi=None):
    if N is None and n is None and Yi is None:
        n, N = dowell_sample_size()
        Yi_input = input("Enter the population values(comma separated): ")
        # assumes values are integers
        Yi = [int(i) for i in Yi_input.split(",")]

    # inscribe the circle randomly by starting from a random index
    start = randrange(0, N)
    Yi = Yi[start:] + Yi[:start]

    # partition the population list into 3 parts corresponding to the areas
    # where the triangle touches the circle x, y and z are the three regions
    # in which the triangle will rotate
    partition = N // 3
    x, y, z = (
        Yi[:partition],
        Yi[partition : (2 * partition)],
        Yi[(2 * partition) :],
    )

    # pick the first value and rotate the lists(x, y and z) by 1
    sample = []
    for _ in range(n // 3):
        sample.append([x[0], y[0], z[0]])
        # rotate by 1 value
        x = x[1:] + x[:1]
        y = y[1:] + y[:1]
        z = x[1:] + z[:1]
    return sample


if __name__ == "__main__":
    print(dowell_geometrical_function())

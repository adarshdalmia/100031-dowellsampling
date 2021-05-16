from random import randrange
from sample_size import dowell_sample_size


def dowell_random_generation(N=None, n=None, Yi=None):
    if N is None and n is None and Yi is None:
        n, N = dowell_sample_size()
        Yi_input = input("Enter the population values(space separated): ")
        Yi = [int(i) for i in Yi_input.split()]
    rand_nos = [randrange(0, N) for _ in range(n)]
    return [Yi[i] for i in rand_nos]


if __name__ == "__main__":
    print(dowell_random_generation())

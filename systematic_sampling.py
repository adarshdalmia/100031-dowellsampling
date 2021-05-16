from sample_size import dowell_sample_size
from random import randint, uniform


def dowell_systematic_sampling():
    n, N = dowell_sample_size()
    Yi_input = input("Enter the population values(space separated): ")
    Yi = [int(i) for i in Yi_input.split()]

    # check if N divides n without remainder
    if N % n == 0:
        k = N // n
        i = randint(0, k)
        print(f"i = {i} k = {k}")
        # select first unit randomly
        Yi = Yi[i:] + Yi[:i]
        sample_units = [Yi[i] for i in range(0, len(Yi), k)]
    else:
        k = N / n
        i = round(uniform(0, k))
        Yi = Yi[i:] + Yi[:i]
        sample_units = [Yi[i] for i in range(0, len(Yi), k)]
    return sample_units


if __name__ == "__main__":
    print(dowell_systematic_sampling())

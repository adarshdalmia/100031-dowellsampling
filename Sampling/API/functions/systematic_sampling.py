from sampleSize import dowellSampleSize
from random import randrange, uniform


def dowellSystematicSampling():
    n, N = dowellSampleSize()
    Yi_input = input("Enter the population values(comma separated): ")
    # assumes values are integers
    Yi = [int(i) for i in Yi_input.split(",")]

    # check if N divides n without remainder
    if N % n == 0:
        k = N // n
        i = randrange(0, k)
        # select first unit randomly
        Yi = Yi[i:] + Yi[:i]
        sample_units = [Yi[ind] for ind in range(i, N, k)]
    else:
        k = N / n
        i = round(uniform(0, k))
        if i > N:
            i -= 1
        # select first unit randomly
        Yi = Yi[i:] + Yi[:i]
        sample_units = [Yi[ind] for ind in range(i, N, k)]
    return sample_units


if __name__ == "__main__":
    print(dowell_systematic_sampling())

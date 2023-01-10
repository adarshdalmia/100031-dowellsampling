from random import randrange

def dowellRandomGeneration(N, n, Yi):
    rand_nos = [randrange(0, N) for _ in range(n)]
    sampleUnits = [Yi[i] for i in rand_nos] 
    return sampleUnits
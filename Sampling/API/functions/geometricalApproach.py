from random import randrange

def dowellGeometricalFunction(N, n, Yi):
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
    sampleUnits = []
    for _ in range(n // 3):
        sampleUnits.append([x[0], y[0], z[0]])
        # rotate by 1 value
        x = x[1:] + x[:1]
        y = y[1:] + y[:1]
        z = x[1:] + z[:1]
    return sampleUnits


if __name__ == "__main__":
    print(dowell_geometrical_function())

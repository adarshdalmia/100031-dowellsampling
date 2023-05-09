def dowellSampleSize(N, e):
    n = int(N / (1 + N * e * e))
    print(n)
    if n > 1 and n < 500:
        return n
    else:
        return "Sample size is not adequate"
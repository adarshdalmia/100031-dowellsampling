"""
Not Implemented:
"If there are more than one category or subset,
Minimum sample size for each subset should be atleast 30
"
"""


def dowell_sample_size():
    while True:
        try:
            N = int(input("Enter the population size: "))
            e = float(input("Enter the error: "))
            n = int(N / (1 + N * e * e))
            if n > 30 and n < 500:
                break
            else:
                print(f"Sample size is not adequate n = {n}")
        except ValueError:
            print("Please enter a digit")
    return n, N


if __name__ == "__main__":
    print(dowell_sample_size())

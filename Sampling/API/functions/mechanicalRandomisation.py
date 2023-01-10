from random import randint

def dowellRandomTable(N, n, Yi):
    sampleUnits = []
    page_no = int(input("Enter the number of pages: "))
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    for _ in range(n):
        rand_page = randint(1, page_no)
        rand_row = randint(1, rows)
        rand_col = randint(1, columns)
        a = f"Enter the number in page: {rand_page} row: {rand_row} column: {rand_col}: "
        random_no = int(input(a))

        # check if random_no is greater than N eg if random_no = 0234 and
        # N is 100 pick the first 3 digits (023)
        if random_no > N:
            rand_len = len(str(N))
            # Pick the first N digits.
            rand_index = int(str(random_no)[:rand_len])
            # check if random_no is greater than N eg if random_no = 123456 and
            # N is 100 pick the first 3 digits (123)
            # eg 123 > 100
            if rand_index >= N:
                rand_index %= N
        else:
            rand_index = random_no
        sampleUnits.append(Yi[rand_index])
    return sampleUnits


if __name__ == "__main__":
    print(dowell_random_table())

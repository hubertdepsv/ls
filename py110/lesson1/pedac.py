# row number n starts with integer s and contains n numbers
# its start integer is equal to the sum of all integers before it
# start_integer = sum([sum(s) for s in range(1, n)])

def sum_even_number_row(row_number):
    rows = []
    start_integer = 2
    for row_length in range(1, row_number + 1):
        row = create_row(start_integer, row_length)
        rows.append(row)
        start_integer = row[-1] + 2
    return sum(rows[-1])


def create_row(start_integer, row_length):
    row = []
    current_integer = start_integer
    while len(row) < row_length:
        row.append(current_integer)
        current_integer += 2
    return row

print(sum_even_number_row(1) == 2) 
print(sum_even_number_row(2) == 10)
print(sum_even_number_row(4) == 68)

print(create_row(2, 1) == [2])
print(create_row(4, 2) == [4, 6])
print(create_row(8, 3) == [8, 10, 12])

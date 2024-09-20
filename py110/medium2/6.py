def sum_square_difference(count):
    square_of_sum = sum(list(range(1, count + 1))) ** 2
    sum_of_squares = sum([num ** 2 for num in range(1, count + 1)])
    return square_of_sum - sum_of_squares

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True
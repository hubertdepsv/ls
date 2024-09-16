def multiply_list(lst):
    for index in range(len(lst)):
        lst[index] *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])
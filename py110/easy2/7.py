def multiply_list(list1, list2):
    res = []
    for a, b in zip(list1, list2):
        res.append(a * b)
    return res

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
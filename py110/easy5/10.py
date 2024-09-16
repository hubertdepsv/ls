def unique_sequence(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return result

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True
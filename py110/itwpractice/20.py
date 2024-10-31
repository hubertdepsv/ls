def what_is_different(lst):
    average = sum(lst) / len(lst)

    unique_values = set(lst)
    first_value = unique_values.pop()
    second_value = unique_values.pop()

    first_try = max(first_value - average, average - first_value)
    second_try = max(second_value - average, average - second_value)
    
    if first_try > second_try:
        return first_value
    else:
        return second_value



print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)
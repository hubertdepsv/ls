def minimum_sum(lst):
    minimum = float("inf")
    n = len(lst)

    if n < 5:
        return None
    
    for index in range(n - 5 + 1):
        current_sum = sum(lst[index:index + 5])
        if current_sum < minimum:
            minimum = current_sum
        
    return minimum

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)
# algorithm

def closest_numbers(lst):
    smallest_difference = float("inf")
    numbers = []
    for index in range(len(lst) - 1):
        for num in lst[index + 1:]:
            diff = -min(lst[index] - num, num - lst[index])
            if diff < smallest_difference:
                smallest_difference = diff
                numbers.append((lst[index], num))
    return numbers[-1]
    

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))
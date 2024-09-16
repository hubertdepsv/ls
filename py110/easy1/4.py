def running_total(lst):
    if len(lst) == 0:
        return []
    cumulative_sum = [lst[0]]
    for index, num in enumerate(lst[1:]):
        cumulative_sum.append(cumulative_sum[index] + num)
    return cumulative_sum

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
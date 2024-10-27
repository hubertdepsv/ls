# Inputs: lst of numbers
# Output: lst of numbers
# Count unique values instead of numbers
# Data structure: set to get unique values, list otherwise
# for each number in the input list
# determine how many values are smaller that it in the list - subpb
# place the answer in a list

def smaller_numbers_than_current(lst):
    result = []
    for pivot in lst:
        result.append(len(set([number for number in lst if number < pivot])))
    return result

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)
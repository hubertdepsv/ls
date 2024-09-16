# - Input: list of strings
# - Output: a list of strings sorted according to the highest number
#   of adjacent consonants

# - Remove the spaces from the "input string".
# - Initialize a "maximum consonants count" to zero.
# - Initialize an "adjacent consonants string" to an empty string.
# - For each "letter" in the "input string":
#     - If the "letter" is a consonant:
#         - Concatenate it to the "adjacent consonants string".
#     - If the "letter" is a vowel:
#         - If the "adjacent consonants string" has a length
#           greater than the current "maximum consonants count":
#             - If the "adjacent consonants string" has a length
#               greater than 1:
#                 - Set the "maximum consonants count" to the length
#                   of the "adjacent consonants string".

#         - Reset the "adjacent consonants string" to an empty string.

# - Return the "maximum consonants count".

def sort_by_consonant_count(lst):

    lst.sort(key=count_max_adjacent_consonants, reverse=True, )
    return lst

def count_max_adjacent_consonants(string):
    string = ''.join(string.split(' '))
    maximum_consonants_count = 0
    adjacent_consonants_string = ''
    for char in string:
        if char not in ['a', 'e', 'i', 'o', 'u']:
            adjacent_consonants_string += char
            if len(adjacent_consonants_string) > maximum_consonants_count:
                if len(adjacent_consonants_string) > 1:
                    maximum_consonants_count = len(adjacent_consonants_string)
        else:
            if len(adjacent_consonants_string) > maximum_consonants_count:
                if len(adjacent_consonants_string) > 1:
                    maximum_consonants_count = len(adjacent_consonants_string)
            adjacent_consonants_string = ''

    return maximum_consonants_count


# print(count_max_adjacent_consonants('dddaa'))       # 3
# print(count_max_adjacent_consonants('ccaa'))        # 2
# print(count_max_adjacent_consonants('baa'))         # 0
# print(count_max_adjacent_consonants('aa'))          # 0
# print(count_max_adjacent_consonants('rstafgdjecc')) # 4

print(sort_by_consonant_count(['aa', 'baa', 'ccaa', 'dddaa']) == ['dddaa', 'ccaa', 'aa', 'baa'])
print(sort_by_consonant_count(['can can', 'toucan', 'batman', 'salt pan']) == ['salt pan', 'can can', 'batman', 'toucan'])
print(sort_by_consonant_count(['bar', 'car', 'far', 'jar']) == ['bar', 'car', 'far', 'jar'])
print(sort_by_consonant_count(['day', 'week', 'month', 'year']) == ['month', 'day', 'week', 'year'])
print(sort_by_consonant_count(['xxxa', 'xxxx', 'xxxb']) == ['xxxx', 'xxxb', 'xxxa'])
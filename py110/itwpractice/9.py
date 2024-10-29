def count_substrings(string, substring):
    if string.find(substring) == -1:
        return 0
    
    count = 0
    new_string = string
    while len(new_string) > 0:
        starting_index = new_string.rfind(substring)
        if starting_index == -1:
            break
        new_string = new_string[:starting_index]
        count += 1

    return count


print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)
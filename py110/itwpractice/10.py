def even_substrings(string):
    # get all substrings
    substrings = []
    for start in range(len(string)):
        for end in range(start, len(string) + 1):
            if start != end:
                substrings.append(string[start:end])

    # count those that are even
    even_count = 0
    even_substrings = []
    for substring in substrings:
        if int(substring) % 2 == 0:
            even_count += 1
            even_substrings.append(substring)

    return even_count


print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)
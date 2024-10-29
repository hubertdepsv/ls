def most_common_char(string):
    string = string.lower()
    frequencies = {}
    for char in string:
        if char in frequencies.keys():
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    # get the max
    max_freq = 0
    most_frequent_letter = ''
    for letter in frequencies.keys():
        if frequencies[letter] > max_freq:
            max_freq = frequencies[letter]
            most_frequent_letter = letter

    return most_frequent_letter

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')
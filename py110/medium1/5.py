def word_to_digit(message):
    NUMBERS = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    lst = message.split()
    result = []
    for word in lst:
        result.append(NUMBERS.get(word, word))
    return ' '.join(result)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True
import math

def letter_percentages(string):
    lowercase = 0
    uppercase = 0
    neither = 0
    string_len = len(string)
    for char in string:
        if char.isalpha():
            if char == char.lower():
                lowercase += 1
            elif char == char.upper():
                uppercase += 1
        else:
            neither += 1
    return {
        'lowercase': f"{(lowercase / string_len * 100):.2f}",
        'uppercase': f"{(uppercase / string_len * 100):.2f}",
        'neither': f"{(neither / string_len * 100):.2f}",
    }

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
def string_to_signed_integer(s):
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    value = 0
    sign = 1

    if s[0] not in DIGITS:
        if s[0] == '-':
            s = s[1:]
            sign *= -1
        elif s[0] == '+':
            s = s[1:]

    for char in s:
        value = (10 * value) + DIGITS[char]

    return value * sign

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
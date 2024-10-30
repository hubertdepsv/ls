def repeated_substring(string):
    factor = len(string) // len(set(list(string)))
    return (string[:len(string) // factor], factor)
    
print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))
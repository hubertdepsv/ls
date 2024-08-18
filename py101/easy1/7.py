def short_long_short(string_a, string_b):
    len_a, len_b = len(string_a), len(string_b)
    # we assume the strings never have the same length
    if len_a < len_b:
        return string_a + string_b + string_a
    else:
        return string_b + string_a + string_b
    
# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")
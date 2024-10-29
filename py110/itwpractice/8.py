def longest_vowel_substring(string):
    VOWELS = 'aeiou'
    max_vowel_substring_length = 0
    current_vowel_substring_length = 0
    for char in string:
        if char in VOWELS:
            current_vowel_substring_length += 1
        else:
            current_vowel_substring_length  = 0
        max_vowel_substring_length = max(
            max_vowel_substring_length, current_vowel_substring_length
        )
    return max_vowel_substring_length

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)
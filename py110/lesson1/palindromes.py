"""
PROBLEM:

Given a string, write a function `change_me` which returns the same
string but with all the words in it that are palindromes uppercased.
"""

# PEDAC
# Input: string
# Output: string
# Explicit: 
# Implicit: palindromes are not case-sensitive

# Data structure: nothing specific, apart from strings

# Algorithm:
# Create an empty string to contain the result
# Split it into words
# Iterate over the list of words to find palindromes
# If the current word is a palindrome, upper case it
# Join the words in the list into a string and return it

# Comments show expected return values
print(change_me("We will meet at noon"))       # "We will meet at NOON"
print(change_me("No palindromes here"))        # "No palindromes here"
print(change_me(""))                           # ""
print(change_me("I LOVE mom and dad equally")) # "I LOVE MOM and DAD equally"
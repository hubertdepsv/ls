"""
A double number is an even-length number whose left-side digits 
are exactly the same as its right-side digits. For example, 44, 
3333, 103103, and 7676 are all double numbers, whereas 444, 
334433, and 107 are not.

Write a function that returns the number provided as an argument 
multiplied by two, unless the argument is a double number. If the 
argument is a double number, return the double number as-is.
"""

def twice(number):
    string = str(number)
    n = len(number)
    if len(string) % 2 != 0:
        return number * 2
    elif string[:n] == string[n:]:
        return number
    else:
        return number * 2
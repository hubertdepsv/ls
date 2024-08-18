"""
Write a function that computes the sum of all numbers between 1 and some other number, 
inclusive, that are multiples of 3 or 5. For instance, if the supplied number is 20, 
the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

You may assume that the number passed in is an integer greater than 1.
"""

def multisum(number):
    sum = 0
    for i in range(1, number + 1):
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
        else:
            continue
    return sum

# mode modular solution
def is_multiple(number, divisor):
    return number % divisor == 0

def multisum(max_value):
    total_sum = 0
    for number in range(1, max_value + 1):
        if is_multiple(number, 3) or is_multiple(number, 5):
            total_sum += number
    return total_sum

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
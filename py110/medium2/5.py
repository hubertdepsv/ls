def has_unique_digits(number):
    digits = list(str(number))
    return len(set(digits)) == len(digits)

def to_next_odd_multiple_of_seven(number):
    number += 1
    while number % 2 != 1 or number % 7 != 0:
        number += 1
    return number

def next_featured(number):
    MAX_FEATURED = 9876543201
    featured_num = to_next_odd_multiple_of_seven(number)
    while number <= MAX_FEATURED:
        if has_unique_digits(featured_num):
            return featured_num
        featured_num += 14
    
    return "There is no possible number that fulfills those requirements."

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True
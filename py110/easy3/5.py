def reverse_number(integer):
    lst = list(str(integer))
    lst.reverse()
    return int(''.join(lst))
    # return int(str(number)[::-1])

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True
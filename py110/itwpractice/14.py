def seven_eleven(number):
    sum_lst = 0
    for num in range(number):
        if num % 7 == 0 and num % 11 == 0:
            sum_lst += num
        elif num % 7 == 0 or num % 11 == 0:
            sum_lst += num
    return sum_lst


print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)
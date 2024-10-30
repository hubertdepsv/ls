def greatest_product(string):
    # find max 4 numbers
    max_number = 0
    for index in range(len(string) - 3):
        max_number = max(max_number, int(string[index:index+4]))
    product = 1
    for char in str(max_number):
        product *= int(char)
    return product


print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6
def max_rotation(number):
    lst = list(str(number))
    lst = lst[1:] + [lst[0]]
    for index in range(1, len(lst) - 1):
        lst = lst[:index] + lst[(index+1):] + [lst[index]]
    return int(''.join(lst))


print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True
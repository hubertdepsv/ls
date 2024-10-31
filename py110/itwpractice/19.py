def odd_fellow(lst):
    # compute frequencies
    frequencies = {}
    for num in lst:
        if str(num) in frequencies.keys():
            frequencies[str(num)] += 1
        else:
            frequencies[str(num)] = 1

    for num in frequencies.keys():
        if frequencies[num] % 2 == 1:
            return int(num)

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)
def pairs(lst):
    if not lst or len(lst) < 1:
        return 0
    
    # get frequencies
    frequencies = {}
    for num in lst:
        str_num = str(num)
        if str_num in frequencies.keys():
            frequencies[str_num] += 1
        else:
            frequencies[str_num] = 1

    # find out which frequencies are multiples of 2
    number_of_pairs = 0
    for number in frequencies.keys():
        if frequencies[number] > 0:
            number_of_pairs += (frequencies[number] // 2)
    return number_of_pairs

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
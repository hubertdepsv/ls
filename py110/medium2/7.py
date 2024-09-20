def bubble_sort(lst):
    while True:
        swap_count = 0
        for index in range(1, len(lst)):
            if lst[index - 1] > lst[index]:
                swap_count += 1
                lst[index - 1], lst[index] = lst[index], lst[index - 1]
            else:
                continue
        if swap_count == 0:
            break
    return lst


lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True
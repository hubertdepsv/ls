def interleave(lst1, lst2):
    res = []
    for a, b in zip(lst1, lst2):
        res.append(a)
        res.append(b)
    return res

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2))# == expected)      # True
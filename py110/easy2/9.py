def count_occurrences(lst):
    res = {}
    for item in lst:
        res[item] = res.get(item, 0) + 1
    return res


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

print(count_occurrences(vehicles))
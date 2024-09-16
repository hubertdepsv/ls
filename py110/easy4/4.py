def order_by_value(dct):
    return sorted(list(dct.keys()), key=dct.get)

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
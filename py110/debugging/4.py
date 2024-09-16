def get_key_value(my_dict, key):
    return my_dict.get(key, f"{key} not in input dict")
    if my_dict[key]:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))
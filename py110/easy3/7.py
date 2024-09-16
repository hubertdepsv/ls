def swap_name(name):
    first_name = name.split(' ')[0]
    last_name = name.split(' ')[1]
    return f"{last_name}, {first_name}"
    
print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
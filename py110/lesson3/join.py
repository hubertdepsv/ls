def join_or(lst, delimiter=', ', word='or'):
    str_lst = [str(num) for num in lst]
    if len(str_lst) == 0:
        return ""

    if len(str_lst) == 1:
        return str_lst[0]
    
    return f"{delimiter.join(str_lst[:-1])} {word} {str_lst[-1]}"

print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"
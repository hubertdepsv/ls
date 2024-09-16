def staggered_case(string):
    if len(string) < 1:
        return ""
    
    result = []
    for idx, char in enumerate(string.lower()):
        if (idx % 2 == 0):
            result.append(char.capitalize())
        else:
            result.append(char)
    return ''.join(result)

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
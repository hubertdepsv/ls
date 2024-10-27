# every 2nd character in every 3rd word uppercased

def to_weird_case(string):
    lst = string.split()
    result = []
    for index, word in enumerate(lst):
        if (index + 1) % 3 == 0 and len(word) >= 2:
            word = ''.join([char.upper() if idx % 2 == 1 else char for idx, char in enumerate(word)])
            result.append(word)
        else:
            result.append(word)
    return ' '.join(result)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)
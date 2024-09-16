def word_swap(string):
    result = ''
    if len(string) > 2:
        result = ''.join([string[-1], string[1:-1], string[0]])
    else:
        result = string[::-1]
    return result

def swap(sentence):
    words = sentence.split(' ')
    result = []
    for word in words:
        result.append(word_swap(word))
    return ' '.join(result)

print(swap('Oh what a wonderful day it is')
       == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
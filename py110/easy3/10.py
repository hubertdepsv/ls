def is_balanced(string):
    track = []
    for char in string:
        if char == '(':
            track.append(char)
        elif char == ')':
            if track and track[-1] == '(':
                track.pop()
            else:
                track.append(char)
    return len(track) == 0

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
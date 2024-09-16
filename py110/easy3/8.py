def sequence(count, start):
    if start == 0:
        return [0 for _ in range(count)]
    
    sign = int(start / abs(start))
    return list(range(start, start * count + sign * 1, start))

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True
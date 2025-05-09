def transpose(matrix):
    result = [[], [], []]
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            result[i].append(matrix[j][i])
    return result

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True
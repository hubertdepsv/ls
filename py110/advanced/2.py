def transpose(matrix):
    m = len(matrix[0])
    n = len(matrix)
    # populate empty matrix
    result = [[] for _ in range(m)]
    # number of columns should be previous number of rows
    # 1 <= i <= n
    # 1 <= j <= m
    n = len(matrix)
    for i in range(m):
        for j in range(n):
            result[i].append(matrix[j][i])
    return result

# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)
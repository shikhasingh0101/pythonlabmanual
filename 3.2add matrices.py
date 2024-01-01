
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result_matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]


print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nSum of Matrices:")
for row in result_matrix:
    print(row)

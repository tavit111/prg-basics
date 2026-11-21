###
# Returns a transposed matrix
#
def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])

    transposed = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            # moving rows to columns
            transposed[j][i] = m[i][j]

    return transposed


# Prints a 2D array in rows and columns
def print_matrix(m):
    for row in m:
        for number in row:
            print(number, end=" ")
        print()


# Matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix3 = [
    [5, 6, 7, 8]
]

# Print transposed matrices
print("Matrix 1:")
print_matrix(transpose_matrix(matrix1))

print("\nMatrix 2:")
print_matrix(transpose_matrix(matrix2))

print("\nMatrix 3:")
print_matrix(transpose_matrix(matrix3))
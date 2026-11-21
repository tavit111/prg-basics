###
# Replaces the main diagonal values with 1
#
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Change main diagonal values
for i in range(len(matrix)):
    matrix[i][i] = 1

# Print modified matrix
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
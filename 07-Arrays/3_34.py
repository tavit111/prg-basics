###
# Creates an identity matrix of size n
#
def identity_matrix(n):
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        matrix[i][i] = 1

    return matrix


# Prints a 2D array in rows and columns
def print_matrix(matrix):
    for row in matrix:
        for number in row:
            print(number, end=" ")
        print()


# Print identity matrices of sizes 3, 5 and 8
print("Identity matrix 3x3:")
print_matrix(identity_matrix(3))

print("\nIdentity matrix 5x5:")
print_matrix(identity_matrix(5))

print("\nIdentity matrix 8x8:")
print_matrix(identity_matrix(8))
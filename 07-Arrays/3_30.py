###
# Creates a multiplication table
#
numbers = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Create multiplication table
for i in range(5):
    for j in range(5):
        numbers[i][j] = (i + 1) * (j + 1)

# Print array
for row in numbers:
    for number in row:
        print(f"{number:2}", end=" ")
    print()
###
# Swaps the first and last columns of a 2D array
#
numbers = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# Print original array
print("Original array:")

for row in numbers:
    for number in row:
        print(f"{number:2}", end=" ")
    print()

# Swap first and last columns
for row in numbers:
    row[0], row[-1] = row[-1], row[0]

# Print modified array
print("\nModified array:")

for row in numbers:
    for number in row:
        print(f"{number:2}", end=" ")
    print()
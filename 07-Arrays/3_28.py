###
# Calculates the sum of values in the last column
#
numbers = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

total = 0

for row in numbers:
    total += row[-1]

print("Sum of the last column:", total)
###
# Finds the smallest and largest values in a 2D array
# and their positions
#
numbers = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

min_value = numbers[0][0]
max_value = numbers[0][0]

min_row = 0
min_col = 0
max_row = 0
max_col = 0

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] < min_value:
            min_value = numbers[i][j]
            min_row = i
            min_col = j

        if numbers[i][j] > max_value:
            max_value = numbers[i][j]
            max_row = i
            max_col = j

print("Smallest value:", min_value)
print("Row:", min_row + 1, "Column:", min_col + 1)

print("Largest value:", max_value)
print("Row:", max_row + 1, "Column:", max_col + 1)
###
# Converts a 2D array into a 1D array
#
def convert_to_1d(array):
    result = []

    for row in array:
        for number in row:
            result.append(number)

    return result


# Arrays to convert
array1 = [
    [2, 3],
    [1, 5]
]

array2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

array3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

# Print converted arrays
print("Array 1:", convert_to_1d(array1))
print("Array 2:", convert_to_1d(array2))
print("Array 3:", convert_to_1d(array3))
###
# Checks if the first array is a subset of the second array
#
array1 = [2, 4, 6]
array2 = [1, 2, 3, 4, 5, 6, 7]

is_subset = True

for number in array1:
    if number not in array2:
        is_subset = False
        break

print("Array 1:", array1)
print("Array 2:", array2)
print("Is array 1 a subset of array 2?", is_subset)
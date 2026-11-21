###
# Sorts an array using the Bubble Sort algorithm
#
def bubblesort(array):
    n = len(array)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


# Testing the bubblesort function
print("Array 1:", bubblesort([8, 3, 5, 1, 9, 2]))
print("Array 2:", bubblesort([34, 7, 19, 4, 21, 8]))
print("Array 3:", bubblesort([15, -8, 31, -47, 2, 19]))
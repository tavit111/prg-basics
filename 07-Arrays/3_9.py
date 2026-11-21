###
# Compares two arrays
# Returns True if both arrays are the same - same length and items of the same position
#
def compare(array1, array2):
    if len(array1) != len(array2):
        return False

    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False

    return True


# Test compare function
print("Array 1:", compare(["water", "book", "sky"], ["water", "book", "sky"]))
print("Array 2:", compare([True, False], [True, False, True]))
print("Array 3:", compare([5, 3, 1], [5, 3, 1]))
print("Array 4:", compare([3, 2, 1], [3, 2]))
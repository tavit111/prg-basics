###
# Functions for operating on arrays of numbers
#

# Returns the number of elements
def array_length(array):
    count = 0
    for number in array:
        count += 1
    return count


# Returns a sorted copy of an array
def bubble_sort(array):
    arr = array[:]
    n = array_length(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Returns the second largest number
def second_largest(array):
    arr = bubble_sort(array)

    for i in range(array_length(arr) - 2, -1, -1):
        if arr[i] < arr[-1]:
            return arr[i]


# Returns the difference between largest and smallest values
def difference(array):
    arr = bubble_sort(array)
    return arr[-1] - arr[0]


# Returns the median
def median(array):
    arr = bubble_sort(array)
    n = array_length(arr)

    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


# Returns smallest and largest values
def min_max(array):
    arr = bubble_sort(array)
    return [arr[0], arr[-1]]


# Returns array elements separated by minus signs
def array_to_string(array):
    result = ""

    for number in array:
        if result != "":
            result += "-"
        result += f"{number}"

    return result
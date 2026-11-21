###
# Sorts an array using the bubble sort algorithm
#
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


numbers = [5, 2, 8, 1, 3]

print("Before sorting:", numbers)
print("After sorting:", bubble_sort(numbers))
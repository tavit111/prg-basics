###
# Modifies array elements acording to the instruction
#
arr = [1, 2, 3, 4, 5]

print("Array:", arr)

# Subtract 1 from the first element
arr[0] -= 1
print("Array:", arr)

# Increase the last element by 4
arr[-1] += 4
print("Array:", arr)

# Multiply the middle element by 2
arr[len(arr) // 2] *= 2
print("Array:", arr)
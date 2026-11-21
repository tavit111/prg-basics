###
# Prints an array in reverse order
#
numbers = [15, 8, 31, 47, 2, 19]


print("reverse array:", end=" ")
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i], end=" ")
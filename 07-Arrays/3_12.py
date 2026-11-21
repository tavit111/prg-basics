###
# Prints unique elements in an array
#
numbers = [2, 3, 2, 5, 8, 1, 9, 8]

print("Array:", end=" ")
for number in numbers:
    print(number, end=" ")

print()

print("Unique elements:", end=" ")
for number in numbers:
    if numbers.count(number) == 1:
        print(number, end=" ")
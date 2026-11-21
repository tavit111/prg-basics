###
# Finds the maximum and minimum values in an array
# Without using min() and max()
#
numbers = [-15, 8, -31, 47, -2, 19]

min_value = numbers[0]
max_value = numbers[0]

for number in numbers:
    if number < min_value:
        min_value = number

    if number > max_value:
        max_value = number

print("Minimum number:", min_value)
print("Maximum number:", max_value)
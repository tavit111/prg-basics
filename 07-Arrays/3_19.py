###
# Counts numbers greater than a given value
#
numbers = [3.5, 7.2, 1.8, 9.4, 5.6, 2.1, 8.3]

value = float(input("Enter a value: "))

counter = 0

for number in numbers:
    if number > value:
        counter += 1

print("Array:", *numbers)
print("Given value:", value)
print("Number of elements greater than the given value:", counter)
###
# Calculates the arithmetic mean of array values
#
numbers = [15, 8, 31, 47, 2, 19]

total = 0

for number in numbers:
    total += number

mean = total / len(numbers)

print("Array:", end=" ")
for number in numbers:
    print(number, end=" ")

print()
print(f"Arithmetic mean: {mean:.2f}")
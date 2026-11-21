###
# Calculates the arithmetic mean of array values
#
numbers = [15, 8, 31, 47, 2, 19]

total = 0
i = 0

while i < len(numbers):
    total += numbers[i]
    i += 1

mean = total / len(numbers)

print("Array:", end=" ")

i = 0
while i < len(numbers):
    print(numbers[i], end=" ")
    i += 1

print()
print(f"Arithmetic mean: {mean:.2f}")
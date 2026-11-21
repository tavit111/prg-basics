###
# Separates even and odd numbers in an array
#
arr = [7, 9, 2, 4, 5, 6]

even_numbers = []
odd_numbers = []

for number in arr:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Original array:", arr)

arr = even_numbers + odd_numbers

print("Modified array:", arr)
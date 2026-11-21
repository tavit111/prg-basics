###
# Tests functions from MyArrays module
#
import MyArrays

numbers = [7, 3, 8, 5, 2]

print("Numbers:", ",".join(f"{n}" for n in numbers))

print("Second largest number:", MyArrays.second_largest(numbers))
print("Difference:", MyArrays.difference(numbers))
print("Median:", MyArrays.median(numbers))

smallest_largest = MyArrays.min_max(numbers)
print("Smallest and largest number:", f"{smallest_largest[0]},{smallest_largest[1]}")

print("Numbers as a string:", MyArrays.array_to_string(numbers))


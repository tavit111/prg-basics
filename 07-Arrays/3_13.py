###
# Checks if a number occurs in an array
#
def occurs(number, array):
    for value in array:
        if value == number:
            return True

    return False


numbers = [15, 38, 7, 23, 14]

number = int(input("Number: "))

print("Array:", *numbers)

if occurs(number, numbers):
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appear in the array")
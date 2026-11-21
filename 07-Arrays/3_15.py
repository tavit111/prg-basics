###
# Prints a tuple in reverse order
#
numbers = (10, 20, 30, 40, 50)

print("Tuple:", ",".join(str(number) for number in numbers))

reversed_numbers = numbers[::-1]

print("Reverse order:", ",".join(str(number) for number in reversed_numbers))
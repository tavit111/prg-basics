###
# RPN calculator using a stack
# E.g. 2 4 1 + * = is the same as 2 * (4 + 1)
#
stack = []

print("RPN CALCULATOR")
print("Enter numbers, operators (+ - * /) or =")

while True:
    value = input("Enter value: ")

    if value == "=":
        if len(stack) == 1:
            print("Result:", stack.pop())
            break
        else:
            print("Invalid expression")
            break

    elif value in ["+", "-", "*", "/"]:
        if len(stack) < 2:
            print("Not enough numbers")
            break

        b = stack.pop()
        a = stack.pop()

        if value == "+":
            result = a + b
        elif value == "-":
            result = a - b
        elif value == "*":
            result = a * b
        elif value == "/":
            if b == 0:
                print("Cannot divide by zero")
                break
            result = a / b

        stack.append(result)

    else:
        try:
            stack.append(float(value))
        except ValueError:
            print("Invalid value")
            break
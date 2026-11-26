###
# Checks if brackets in an expression are correct
#
import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # Brackets OK
expression2 = "[(2+3]/4)"                  # Brackets incorrect
expression3 = "(2-3*4+(5/6)"               # Brackets incorrect


def brackets_ok(expression):
    stack = queue.LifoQueue()

    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:
        if char in "([{":
            stack.put(char)

        elif char in ")]}":
            if stack.empty():
                return False

            opening = stack.get()

            if opening != brackets[char]:
                return False

    return stack.empty()


print("Expression 1:", brackets_ok(expression1))
print("Expression 2:", brackets_ok(expression2))
print("Expression 3:", brackets_ok(expression3))
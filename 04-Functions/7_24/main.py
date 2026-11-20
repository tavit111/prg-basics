###
# Calculates the value of an arithmetic expression
#
def f(expression):
    result = int(expression[0])
    operator = '+'

    for char in expression[1:]:
        if char == '+' or char == '-':
            operator = char
        else:
            if operator == '+':
                result += int(char)
            elif operator == '-':
                result -= int(char)

    return result


def main():
    print(f("2+3"))
    print(f("3+8+1"))
    print(f("2+3-4+5-0"))


if __name__ == "__main__":
    main()
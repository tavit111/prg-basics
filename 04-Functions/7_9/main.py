###
# Calculates the sum of even or odd digits in a number
#
def f(number, even):
    total = 0

    for digit in str(abs(number)):
        digit = int(digit)

        if even == True and digit % 2 == 0:
            total += digit
        elif even == False and digit % 2 != 0:
            total += digit

    return total


def main():
    print(f(3124, True))
    print(f(3124, False))
    print(f(20576, False))
    print(f(20576, True))
    print(f(13115, True))


if __name__ == "__main__":
    main()
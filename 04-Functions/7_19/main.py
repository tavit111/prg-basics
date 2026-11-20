###
# Calculates the sum of repeated digits in a number
#
def f(number):
    total = 0
    digits = str(number)

    for digit in digits:
        if digits.count(digit) > 1:
            total += int(digit)

    return total


def main():
    print(f(1027))
    print(f(230335))
    print(f(513553007))


if __name__ == "__main__":
    main()
###
# Checks if a given string is a valid binary number
#
def f(binary_number):
    for digit in binary_number:
        if digit != '0' and digit != '1':
            return False

    return len(binary_number) > 0


def main():
    print(f("101101"))
    print(f("1311a10100"))


if __name__ == "__main__":
    main()
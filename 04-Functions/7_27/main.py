###
# Checks if a product code is correct. Have to cosnsist of 4 digits,
# the 4th digit have to be a modal of (sum of first 3 digits) % 7
#
def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False

    total = 0

    for digit in product_code[:3]:
        total += int(digit)

    control_digit = total % 7

    return control_digit == int(product_code[3])


def main():
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))


if __name__ == "__main__":
    main()
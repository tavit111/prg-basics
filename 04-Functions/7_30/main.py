###
# Calculates the sum of natural numbers using recursion
#
def sum_natural(n):

    if n == 0:
        return 0

    return n + sum_natural(n - 1)


def main():
    n = 10
    print(f"The sum of natural numbers from 1 to {n} is {sum_natural(n)}")


if __name__ == "__main__":
    main()
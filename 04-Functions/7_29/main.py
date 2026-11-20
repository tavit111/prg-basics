###
# Calculates the factorial recursively 
#
def factorial(n):

    # 0! = 1, 1! = 1
    if n == 0 or n == 1:
        return 1

    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n - 1)


def main():
    n = 5
    print(f"The factorial of {n} is {factorial(n)}")


if __name__ == "__main__":
    main()
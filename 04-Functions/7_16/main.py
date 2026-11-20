###
# Returns the n-th number of the Fibonacci sequence
#
def f(n):
    a = 0
    b = 1

    # iterate over the remaining n-1 times
    for i in range(n - 1):
        next_number = a + b
        a = b
        b = next_number

    return a


def main():
    print(f(5))
    print(f(9))


if __name__ == "__main__":
    main()
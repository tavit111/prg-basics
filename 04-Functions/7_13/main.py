###
# Returns the range of digits from 1 to n as a string
#
def f(n):
    result = ''

    for i in range(1, n + 1):
        result += str(i)

    return result


def main():
    print(f(11))
    print(f(4))


if __name__ == "__main__":
    main()
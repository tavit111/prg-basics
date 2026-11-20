###
# Returns n amount of asterisks separated by a slash
#
def f(n):
    result = ''

    for i in range(n):
        # check if it is the first asteric
        if i > 0:
            result += '/'
        result += '*'

    return result


def main():
    print(f(4))
    print(f(1))


if __name__ == "__main__":
    main()
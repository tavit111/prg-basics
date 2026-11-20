###
# Calculates the sum of numbers divisible by 2 and 3
# but not divisible by 4
#
def f(x, y):
    total = 0

    for i in range(x, y + 1):
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
            total += i

    return total


def main():
    print(f(1, 20))
    print(f(10, 30))


if __name__ == "__main__":
    main()
###
# Counts the amount of digits that are negative and even in the given range <x, y>
#
def f(x, y):
    count = 0

    for i in range(x, y + 1):
        if i < 0 and i % 2 == 0:
            count += 1

    return count


def main():
    print(f(-7, 8))
    print(f(-1, 11))


if __name__ == "__main__":
    main()
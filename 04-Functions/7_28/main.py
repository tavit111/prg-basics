###
# Returns the dice number rolled the most times in a row
#
def f(dice):
    max_count = 0
    count = 0
    result = ''

    for i in range(len(dice)):
        if i > 0 and dice[i] == dice[i - 1]:
            count += 1
        else:
            count = 1

        if count > max_count:
            max_count = count
            result = dice[i]

    return int(result) if result else None


def main():
    print(f("5233165554211"))
    print(f("2133"))


if __name__ == "__main__":
    main()
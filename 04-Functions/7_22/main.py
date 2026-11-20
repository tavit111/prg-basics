###
# Returns an acronym from the first letters of all words
#
def f(name):
    acronym = ''

    words = name.split()

    for word in words:
        acronym += word[0]

    return acronym


def main():
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))


if __name__ == "__main__":
    main()
###
# Checks if a given text is a palindrome
# (is reading forward and backword the same)
#
def f(palindrome):
    if palindrome == palindrome[::-1]:
        return True
    else:
        return False


def main():
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))


if __name__ == "__main__":
    main()
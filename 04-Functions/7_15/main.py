###
# Checks if at least 3 people were in the room at the same time
# based on + (symbolise person enter the romm) and - (peroson leaving a room)
#
def f(detector):
    people = 0

    for char in detector:
        if char == '+':
            people += 1
        elif char == '-':
            people -= 1

        if people >= 3:
            return True

    return False


def main():
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))


if __name__ == "__main__":
    main()
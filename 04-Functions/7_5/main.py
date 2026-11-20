###
# Checks if a number is within the range <2,15>
#
import numbers

def main():
    number = int(input("A number: "))

    if numbers.is_in_range(number, 2, 15):
        print(f"Number {number} in the range <2,15>: yes")
    else:
        print(f"Number {number} in the range <2,15>: no")


if __name__ == "__main__":
    main()
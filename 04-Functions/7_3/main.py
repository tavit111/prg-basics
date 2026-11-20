###
# Prints the name of a month
#
import months

def main():
    month_number = int(input('Enter month number: '))
    month_name = months.month(month_number)

    print(f'The name of month {month_number} is {month_name}')


if __name__ == "__main__":
    main()
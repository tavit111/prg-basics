###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    abs_number = abs(number)
    total = 0

    for digit in str(abs_number):
        total += int(digit)
    
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')
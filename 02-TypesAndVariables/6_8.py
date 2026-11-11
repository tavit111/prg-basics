###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ').upper()
last = input('Enter last letter: ').upper()

first_letter_code = ord(first)
last_letter_code = ord(last)


number_of_letters = max(abs(last_letter_code - first_letter_code) - 1, 0)

print(f'Between {first} and {last} is {number_of_letters} letters')
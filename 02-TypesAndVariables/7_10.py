###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user tries to guess
# the number from dice by entering a number from 1 to 6.
#
import random

# COMPUTER TURN
computer = random.randint(1, 6)

# YOUR TURN
you = int(input('Guess the number (1-6): '))

won = you == computer

print(f'You won: {won}')
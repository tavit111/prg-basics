###
# A program that checks whether the vehicle speed
# on a highway in Poland is valid.
#
speed = int(input('Enter vehicle speed: '))

speed_valid = speed >= 40 and speed <= 140

print(f'Speed is valid: {speed_valid}')
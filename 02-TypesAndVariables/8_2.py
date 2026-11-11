###
# Calculation of circle area and circumference
#
import math

# determine radius and PI values
r = float(input('Enter radius: '))

# calculate area
area = math.pi * r ** 2

# calculate circumference
circumference = 2 * math.pi * r

# print results
print(f'Area: {area:.2f}')
print(f'Circumference: {circumference:.2f}')
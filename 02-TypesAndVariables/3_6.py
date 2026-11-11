###
# A program that calculates the distance to the horizon
# based on the observer's height.
#
import math

h = float(input("Enter your height in meters: "))
if h <= 0:
    print("The height must be a positive, non-zero number.")
else:
    d = 3.57 * math.sqrt(h)
    print("Distance to the horizon:", d, "km")
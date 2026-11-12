###
# Determines the position of a point in the coordinate system
#
x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
elif x > 0 and y < 0:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")
elif x == 0 and y == 0:
    print(f"Point P({x},{y}) is at the origin of the coordinate system")
elif x == 0:
    print(f"Point P({x},{y}) is on the Y axis")
else:
    print(f"Point P({x},{y}) is on the X axis")
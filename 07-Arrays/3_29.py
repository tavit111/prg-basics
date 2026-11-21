###
# Creates a two-dimensional array filled with zeros
#

# x are rows, y are columns
def create_2d_arr(x, y):
    return [[0 for i in range(y)] for i in range(x)]


numbers = create_2d_arr(3, 5)

for row in numbers:
    for number in row:
        print(number, end=" ")
    print()
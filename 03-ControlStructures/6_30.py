###
# Prints a lottery coupon with numbers from 1 to 49
#
for i in range(1, 8):
    for j in range(7):
        print(f"{i+j*7}", end=" ")
    print()
        
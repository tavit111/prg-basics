##
# Fibanaci sequence
##

first= 0
second = 1

for i in range(1, 21):
    print(first, end=" ")
    temp = first
    first = second
    second += temp
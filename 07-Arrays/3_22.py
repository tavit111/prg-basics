import random

###
# Returns a randomly selected array element
#
def rand_elem(array):
    return random.choice(array)


numbers = [10, 20, 30, 40, 50]

print("Array:", numbers)

for i in range(5):
    print("Random element:", rand_elem(numbers))
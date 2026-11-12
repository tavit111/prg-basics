##
# Find n number of prime numbers
##

n = int(input("How many prime numbers: "))
counter = 2
prime_numers = 0

print("Prime numbers: ", end=" ")

while n > prime_numers:
    is_prime = True

    for i in range(2, counter):
        if counter % i == 0:
            is_prime = False
            break

    if is_prime:
        print(counter, end=" ")
        prime_numers += 1

    counter += 1

print()
###
# Returns the n-th prime number (devide by 0 and itself)
#
def f(n):
    count = 0
    number = 2

    while count < n:
        is_prime = True

        # checking if number variable is prime number
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            count += 1

            if count == n:
                return number

        number += 1


def main():
    print(f(1))
    print(f(5))


if __name__ == "__main__":
    main()
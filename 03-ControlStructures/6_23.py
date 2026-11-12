##
# Multiplication table with the number entered by user
#

user_number = int(input("Enter number: "))

for num in range(1, 11):
    print(f"{user_number} x {num} = {user_number*num}")
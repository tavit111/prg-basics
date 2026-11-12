###
# Checks the PIN code of a payment card
#

correct_pin = "0805"

for i in range(3):
    user_pin = input("Enter the PIN code: ")
    if user_pin == correct_pin:
        break
    print("Incorrect...")
else:
    print("Sorry, your payment card has been blocked.")
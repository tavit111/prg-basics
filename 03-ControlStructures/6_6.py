###
# Parking meter - calculates the parking fee
#
number_hours = int(input("Enter the number of parking hours: "))
fee = 0

if number_hours >= 1 and number_hours <= 2:
    fee = 5
elif number_hours >= 3 and number_hours <=6:
    fee = 15
elif number_hours > 6:
    fee = 20

print(f"The fee is {fee} PLN")
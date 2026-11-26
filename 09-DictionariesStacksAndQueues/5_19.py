###
# Calculates hotel reservation statistics
#
import json


# Returns the number of reserved rooms
def count_rooms(reservations):
    return len(reservations)


# Returns the number of paid reservations
def count_paid(reservations):
    counter = 0

    for reservation in reservations:
        if reservation["paid"]:
            counter += 1

    return counter


# Returns the number of unpaid reservations
def count_unpaid(reservations):
    counter = 0

    for reservation in reservations:
        if not reservation["paid"]:
            counter += 1

    return counter


# Returns the total value of paid reservations
def total_paid(reservations):
    total = 0

    for reservation in reservations:
        if reservation["paid"]:
            total += reservation["nights"] * reservation["price_per_night"]

    return total


# Returns the total value of unpaid reservations
def total_unpaid(reservations):
    total = 0

    for reservation in reservations:
        if not reservation["paid"]:
            total += reservation["nights"] * reservation["price_per_night"]

    return total


# Read JSON file
with open("reservations.json", "r", encoding="utf-8") as file:
    data = json.load(file)

reservations = data["reservations"]

# Print summary
print("HOTEL RESERVATIONS")
print("------------------")
print("Number of rooms:", count_rooms(reservations))
print("Paid reservations:", count_paid(reservations))
print("Unpaid reservations:", count_unpaid(reservations))
print(f"Total value of paid reservations: {total_paid(reservations):.2f}")
print(f"Total value of unpaid reservations: {total_unpaid(reservations):.2f}")
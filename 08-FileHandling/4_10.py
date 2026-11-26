###
# Prints products with price < 60 and stock < 40
#
import csv

with open('clothing.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader)  # Skip the header

    for row in reader:
        product = row[1]
        price = float(row[5])
        stock = int(row[6])

        if price < 60 and stock < 40:
            print(f"{product} - price: {price}, strock: {stock}")

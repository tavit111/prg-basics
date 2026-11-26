###
# Saves product data to a JSON file
#
import json

product = {}

# Read product data from keyboard
product["name"] = input("Product name: ")
product["price"] = round(float(input("Price: ")), 2)
product["paid"] = input("Paid (yes/no): ").lower() == "yes"

# Save product data to JSON file
with open("product.json", "w", encoding="utf-8") as file:
    json.dump(product, file, indent=4)
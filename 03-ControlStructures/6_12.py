###
# Calculates the amount to pay with a 25% discount
# for each product purchased over two
#
number_of_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

if number_of_products > 2:
    amount_to_pay = 2 * product_price + (number_of_products - 2) * product_price * 0.75
else:
    amount_to_pay = number_of_products * product_price

print(f"Amount to pay: {amount_to_pay:.2f}")
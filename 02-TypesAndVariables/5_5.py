###
# A program that calculates the product price
# after applying a discount.
#
price = float(input('Enter price: '))
discount = float(input('Enter discount %: '))

new_price = price * (1 - discount / 100)
reduction = price - new_price

print(f'Original price: {price:.2f}')
print(f'Given discount: {discount:.2f}%')
print(f'Price with discount: {new_price:.2f}')
print(f'Reduction: {reduction:.2f}')
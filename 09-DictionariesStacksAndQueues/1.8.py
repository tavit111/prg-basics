price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

# 1. Lista produktów i ceny przed obniżką
print('Prices before discount:')
for product, price in price_list.items():
    print(f'{product}: {price:.2f}')

# 2. Łączna wartość produktów przed obniżką
total_before = sum(price_list.values())
print(f'Total value before discount: {total_before:.2f}\n')

# 3. Modyfikacja cennika (obniżka o 10% i zaokrąglenie do 2 miejsc po przecinku)
for product, price in price_list.items():
    price_list[product] = round(price * 0.9, 2)

# 4. Lista produktów i ceny po obniżce
print('Prices after 10% discount:')
for product, price in price_list.items():
    print(f'{product}: {price:.2f}')

# 5. Łączna wartość produktów po obniżce
total_after = sum(price_list.values())
print(f'Total value after discount: {total_after:.2f}')

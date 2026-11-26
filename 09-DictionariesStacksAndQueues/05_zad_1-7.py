# slownik z produktami i ich iloscia w sklepie
products = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

# lece petla po slowniku i wypisuje kazdy produkt oraz jego ilosc
for product, quantity in products.items():
    print(f"{product}: {quantity}")

# sumuje wszystkie ilosci ze slownika i wyswietlam wynik
total = sum(products.values())
print(f"\nTotal products in store: {total}")
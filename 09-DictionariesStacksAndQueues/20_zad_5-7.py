# lista słowników z hotelami w Krakowie (każdy element listy to osobny słownik z nazwą i ceną)
hotels_in_Krakow = [
    {"name": "Sky", "price": 320.00},
    {"name": "Metropol", "price": 480.00},
    {"name": "New Port", "price": 420.00},
    {"name": "Aparthotel", "price": 390.00}
]

# lista słowników z hotelami w Sopocie
hotels_in_Sopot = [
    {"name": "Focus", "price": 510.00},
    {"name": "Aqua", "price": 345.00},
    {"name": "La Boutique", "price": 390.00},
    {"name": "Marina", "price": 410.00}
]


# funkcja przyjmująca listę hoteli i zwracająca ich nazwy połączone przecinkiem
def hotel_list(hotels):
    # tworzymy pustą listę, do której wrzucimy same nazwy hoteli
    names = []
    # pętla bierze po kolei każdy pojedynczy słownik (hotel) z przekazanej listy
    for hotel in hotels:
        # wyciągamy wartość spod klucza "name" i dopisujemy do listy 'names'
        names.append(hotel["name"])
    # łączymy wszystkie elementy z listy 'names' w jeden napis, wstawiając między nie przecinek
    return ",".join(names)


# funkcja obliczająca średnią cenę pokoju dla podanej listy hoteli
def avg_price(hotels):
    # zmienna pomocnicza do zsumowania cen wszystkich pokoi
    total = 0
    # pętla przechodzi po kolei przez każdy słownik (hotel) na liście
    for hotel in hotels:
        # wyciągamy cenę spod klucza "price" i dodajemy ją do naszej sumy
        total += hotel["price"]
    # dzielimy sumę przez liczbę hoteli na liście (len(hotels))
    # round() zaokrągla wynik do najbliższej liczby całkowitej
    return round(total / len(hotels))


# obliczamy średnie ceny dla obu miast i zapisujemy je w zmiennych, żeby łatwo je porównać
avg_krakow = avg_price(hotels_in_Krakow)
avg_sopot = avg_price(hotels_in_Sopot)

# wyświetlamy listę hoteli i średnią cenę dla Krakowa
print(f"Hotels in Krakow: {hotel_list(hotels_in_Krakow)}")
print(f"Average hotel price in Krakow: {avg_krakow}")

# wyświetlamy listę hoteli i średnią cenę dla Sopotu
print(f"Hotels in Sopot: {hotel_list(hotels_in_Sopot)}")
print(f"Average hotel price in Sopot: {avg_sopot}")

# porównujemy obie średnie ceny, żeby wskazać miasto z tańszymi hotelami
if avg_krakow < avg_sopot:
    print("Cheaper hotels in: Krakow")
elif avg_sopot < avg_krakow:
    print("Cheaper hotels in: Sopot")
else:
    print("Cheaper hotels in: Both cities have the same average price")
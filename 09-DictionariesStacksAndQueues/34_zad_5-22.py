import json

# otwieramy plik euro json w trybie do odczytu z obsluga polskich znakow
with open('euro.json', 'r', encoding='utf-8') as file:
    # ladujemy zawartosc pliku do zmiennej jako slownik
    data = json.load(file)

# drukujemy naglowek tabeli i linijke oddzielajaca ze znakow rownosci
print(f"{'Date':<16}{'Buying Rate':<16}{'Selling Rate'}")
print("=" * 44)

# przechodzimy przez kazdy kurs na liscie pod kluczem rates
for rate in data['rates']:
    # wyciagamy date kurs kupna bid i kurs sprzedazy ask
    date = rate['effectiveDate']
    buying_rate = rate['bid']
    selling_rate = rate['ask']
    # wyswietlamy dane w rownych kolumnach z czterema miejscami po przecinku
    print(f"{date:<16}{buying_rate:<16.4f}{selling_rate:.4f}")
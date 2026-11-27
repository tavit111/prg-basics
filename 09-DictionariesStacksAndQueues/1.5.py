countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 84000000},
    {"name": "France", "population": 68000000},
    {"name": "Spain", "population": 48000000},
    {"name": "Italy", "population": 59000000}
]

print(f"{'COUNTRY':<10} {'POPULATION'}") #wyrównuje tekst do lewej strony i rezerwuje na niego 10 znaków szerokości, dzięki czemu kolumna POPULATION jest równo ułożona pod nagłówkiem
for country in countries:
    print(f"{country['name']:<10} {country['population']}")

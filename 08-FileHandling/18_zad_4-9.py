# importuje wbudowany modul do wygodnej obslugi plikow CSV
import csv

# nazwa pliku z lista pracownikow
file_name = 'it_company.csv'

# wypisuje naglowek w terminalu
print('GRAPHIC DESIGNERS')
print('=================')

# otwieram plik tylko do odczytu
with open(file_name, 'r', encoding='utf-8') as file:
    # wczytuje kazdy wiersz jako slownik, gdzie kluczami sa nazwy kolumn z naglowka
    reader = csv.DictReader(file)
    # przechodze po kolei przez kazdego pracownika
    for row in reader:
        # sprawdzam, czy stanowisko pracownika to Graphic Designer
        if row['Job Title'] == 'Graphic Designer':
            # wypisuje imie, nazwisko oraz adres e-mail
            print(f"{row['First Name']} {row['Last Name']},{row['Email']}")
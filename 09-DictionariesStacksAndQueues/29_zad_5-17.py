import json

# otwieramy plik json w trybie do odczytu z polskimi znakami
with open('dogs.json', 'r', encoding='utf-8') as file:
    # ładujemy zawartość pliku do zmiennej jako listę słowników
    dogs = json.load(file)

# lecimy po kolei przez każdego psa na liście
for dog in dogs:
    # sprawdzamy czy wiek psa jest poniżej 5 lat
    if dog['age'] < 5:
        # wyciągamy i drukujemy wszystkie dane tego psa
        for key, value in dog.items():
            print(key, ':', value)
        # robimy pustą linijkę dla czytelności
        print()
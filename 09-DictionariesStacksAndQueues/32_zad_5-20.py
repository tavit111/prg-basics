import json

# tworzymy slownik z danymi o ulubionym filmie
favorite_movie = {
    "title": "The Shawshank Redemption",
    "director": "Frank Darabont",
    "release_year": 1994,
    "genre": "Drama",
    "rating": 9.3,
    "main_actors": ["Tim Robbins", "Morgan Freeman"]
}

# ustawiamy nazwe pliku do zapisu
file_name = "favorite.json"

# otwieramy plik do zapisu i wrzucamy tam nasz slownik
# indent 4 robi ladne wciecia zeby plik byl czytelny
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(favorite_movie, file, indent=4)

# wyswietlamy komunikat ze wszystko zapisalo sie poprawnie
print("Data has been written to", file_name)
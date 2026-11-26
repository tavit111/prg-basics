import csv

# funkcja czyszczaca pliki wynikowe przed startem, zeby nie dublowac ksiazek przy kolejnym odpaleniu
def clear_files(files_list):
    for file_name in files_list:
        with open(file_name, 'w', encoding='utf-8') as file:
            pass

# funkcja dopisujaca jedna ksiazke do odpowiedniego pliku
def save_book(file_name, row):
    # otwieram plik w trybie dopisywania ('a'), zeby nie skasowac wczesniej zapisanych ksiazek
    with open(file_name, 'a', encoding='utf-8') as file:
        # sklejam dane ksiazki przecinkami i dodaje enter na koncu
        file.write(','.join(row) + '\n')

# glowna funkcja czytajaca books.csv i rozdzielajaca ksiazki po gatunkach
def sort_books(source_file):
    # slownik laczacy gatunek z nazwa pliku docelowego
    genre_files = {
        'Fantasy': 'books_fantasy.txt',
        'Historical': 'books_historical.txt',
        'Romance': 'books_romance.txt',
        'Classic': 'books_classic.txt'
    }

    # czyszcze wszystkie 4 pliki na starcie
    clear_files(genre_files.values())

    # otwieram plik zrodlowy z ksiazkami
    with open(source_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # pomijam pierwszy wiersz z naglowkami kolumn
        next(reader)

        # przechodze po kolei przez kazda ksiazke
        for row in reader:
            genre = row[2]
            # jesli gatunek pasuje do slownika, zapisuje ksiazke do przypisanego pliku
            if genre in genre_files:
                save_book(genre_files[genre], row)

# odpalam program dla pliku books.csv
sort_books('books.csv')
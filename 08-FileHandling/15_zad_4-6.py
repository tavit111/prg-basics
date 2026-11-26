# pobieram nazwe pliku z klawiatury w terminalu
file_name = input('File name: ')

# blok try zabezpiecza program przed awaria, gdyby plik nie istnial
try:
    # otwieram podany plik tylko do odczytu
    with open(file_name, 'r', encoding='utf-8') as file:
        # wczytuje cala zawartosc pliku do jednej zmiennej
        content = file.read()

        # licze kolejno: wiersze, wszystkie znaki oraz slowa
        num_lines = len(content.splitlines())
        num_chars = len(content)
        num_words = len(content.split())

        # wyswietlam wyniki w terminalu
        print(f'Number of lines: {num_lines}')
        print(f'Number of characters: {num_chars}')
        print(f'Number of words: {num_words}')

# jesli podany plik nie istnieje, program wypisze komunikat zamiast bledu
except FileNotFoundError:
    print(f'File "{file_name}" does not exist.')
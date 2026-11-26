# importuje modul do wyrazen regularnych
import re

# pobieram nazwe uzytkownika i haslo z klawiatury w terminalu
username = input('Enter username: ')
password = input('Enter password: ')

# wzorzec dla loginu: od poczatku (^) do konca ($) tylko male litery [a-z], minimum 6 znakow {6,}
username_pattern = r'^[a-z]{6,}$'

# wzorzec dla hasla: male/duze litery, cyfry lub podkreslnik, minimum 8 znakow {8,}
password_pattern = r'^[a-zA-Z0-9_]{8,}$'

# sprawdzam, czy wpisany login i haslo pasuja do wzorcow
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

# jesli oba warunki sa spelnione, wypisuje sukces, w przeciwnym razie blad
if username_match and password_match:
    print('Username and password are valid.')
else:
    print('Invalid username or password.')
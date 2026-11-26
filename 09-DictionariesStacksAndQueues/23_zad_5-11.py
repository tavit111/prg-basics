# ładujemy wbudowany moduł json, który pozwala odczytywać i zapisywać pliki JSON
import json

# zapisujemy nazwę pliku w zmiennej, żeby nie wpisywać jej kilka razy
file_name = 'vote.json'

# 1. ODCZYT DOTYCHCZASOWYCH WYNIKÓW Z PLIKU JSON
# blok try-except zabezpiecza program przed błędem, gdy uruchomisz go pierwszy raz i plik vote.json jeszcze nie istnieje
try:
    # otwieramy plik vote.json w trybie do odczytu ('r') z obsługą polskich znaków (utf-8)
    with open(file_name, 'r', encoding='utf-8') as file:
        # zamieniamy zawartość pliku JSON na zwykły słownik Pythona i zapisujemy w zmiennej 'votes'
        votes = json.load(file)
except FileNotFoundError:
    # jeśli plik jeszcze nie istnieje na dysku, tworzymy po prostu pusty słownik na głosy
    votes = {}

# 2. POBRANIE GŁOSU OD UŻYTKOWNIKA I AKTUALIZACJA SŁOWNIKA
# pobieramy z klawiatury imię i nazwisko osoby, na którą oddajemy głos
# .strip() usuwa przypadkowe spacje na początku i na końcu tekstu
person_name = input('Name of the person you are voting for: ').strip()

# sprawdzamy, czy podana osoba znajduje się już jako klucz w słowniku 'votes'
if person_name in votes:
    # jeśli osoba ma już jakieś głosy, powiększamy jej licznik o 1
    votes[person_name] += 1
else:
    # jeśli to nowa osoba, dodajemy ją do słownika i ustawiamy liczbę głosów na 1
    votes[person_name] = 1

# 3. ZAPIS ZAKTUALIZOWANYCH WYNIKÓW Z POWROTEM DO PLIKU JSON
# otwieramy plik w trybie do zapisu ('w') — stara zawartość pliku zostanie zastąpiona nową
with open(file_name, 'w', encoding='utf-8') as file:
    # zapisujemy słownik 'votes' do pliku JSON
    # indent=4 sprawia, że plik jest czytelny dla człowieka (ma wcięcia i nowe linie)
    # ensure_ascii=False sprawia, że polskie znaki (np. ł, ś, ć) zapisują się normalnie, a nie jako dziwne kody
    json.dump(votes, file, indent=4, ensure_ascii=False)

# wyświetlamy w terminalu potwierdzenie oraz aktualny stan wszystkich głosów
print(f"Current votes: {votes}")
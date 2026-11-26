# tworzymy słownik, w którym kluczem jest nazwa przedmiotu, a wartością liczba godzin
winter_semester = {
    "math": 60,
    "programming": 30,
    "history": 15
}

# tworzymy zmienną do zliczania wszystkich godzin i ustawiamy ją na 0
total_hours = 0

# pętla przechodzi po kolei przez same wartości ze słownika (czyli 60, 30, 15) dzięki .values()
for hours in winter_semester.values():
    # dodajemy liczbę godzin z bieżącego przedmiotu do naszej sumy
    total_hours += hours

# wyświetlamy końcowy wynik w formacie podanym w poleceniu
print(f"The total number of hours in the winter semester is {total_hours}")
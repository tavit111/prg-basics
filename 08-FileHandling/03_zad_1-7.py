# funkcja otwiera plik i czyta cala zawartosc
def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content

# wczytuje caly plik i dziele go na osobne linijki
file_content = read_from_file('car_park.txt')
file_lines = file_content.splitlines()

# zmienna na sume wszystkich aut
total = 0

# przechodze po kazdej linijce z listy
for line in file_lines:
    # zamieniam tekst na liczbe i dodaje do sumy
    total += int(line)

# wypisuje koncowy wynik
print('Total cars parked:', total)
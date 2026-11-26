# ładujemy moduł queue, żeby móc stworzyć stos
import queue

# tworzymy pusty stos, na którym będziemy odkładać reszty z dzielenia (cyfry 0 i 1)
stack = queue.LifoQueue()

# pobieramy od użytkownika liczbę naturalną i zamieniamy ją z tekstu na liczbę całkowitą (int)
number = int(input("Natural number: "))

# zabezpieczenie na wypadek, gdyby ktoś wpisał po prostu 0
if number == 0:
    stack.put(0)

# pętla działa tak długo, jak liczba jest większa od zera
while number > 0:
    # liczymy resztę z dzielenia przez 2 (znak % daje resztę, czyli zawsze 0 albo 1)
    remainder = number % 2
    # odkładamy obliczoną resztę na samą górę stosu
    stack.put(remainder)
    # dzielimy liczbę całkowicie przez 2 (znak // ucina końcówkę po przecinku)
    number = number // 2

# wypisujemy początek odpowiedzi; end="" sprawia, że kursor nie przeskoczy do nowej linijki
print("Binary number: ", end="")

# zdejmujemy elementy ze stosu od samej góry, dopóki stos nie będzie całkiem pusty
while not stack.empty():
    # pobieramy kolejną cyfrę ze stosu i dopisujemy ją od razu obok poprzedniej
    print(stack.get(), end="")

# na koniec robimy pusty print(), żeby ładnie zamknąć linijkę w terminalu
print()
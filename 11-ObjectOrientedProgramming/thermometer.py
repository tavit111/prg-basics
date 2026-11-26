# importuje wbudowany modul random zeby moc losowac temperature
import random


# klasa Thermometer - moj szablon termometru medycznego trzymany w osobnym pliku
class Thermometer:
    # konstruktor __init__ - odpala sie sam jak tworze nowy termometr
    # self oznacza ten konkretny termometr ktory akurat tworze
    def __init__(self):
        # to sa atrybuty (stany / cechy obiektu) - zmienne przypisane do tego termometru
        self.is_on = False        # atrybut logiczny czy termometr jest wlaczony (na starcie False)
        self.temperature = None   # atrybut na zmierzona temperature (na starcie brak pomiaru - None)

    # to jest metoda (czyli funkcja siedzaca w klasie) - wlacza termometr
    def turn_on(self):
        self.is_on = True

    # metoda wylaczajaca termometr
    def turn_off(self):
        self.is_on = False

    # metoda wykonujaca pomiar - losuje liczbe od 34.0 do 42.0 z dokladnoscia do 0.1
    def measure(self):
        if self.is_on:
            # random.uniform losuje liczbe z ulamkiem, a round(..., 1) zaokragla do 1 miejsca po przecinku
            self.temperature = round(random.uniform(34.0, 42.0), 1)
        else:
            print("Termometr jest wylaczony! Najpierw go wlacz.")

    # metoda wyswietlajaca zmierzona temperature i odpowiednie ostrzezenia
    def display(self):
        if not self.is_on:
            print("Termometr jest wylaczony!")
            return

        if self.temperature is None:
            print("Nie zmierzono jeszcze temperatury!")
            return

        # buduje podstawowy napis z temperatura z atrybutu self.temperature
        info = f"Temperature: {self.temperature}C"

        # jesli temperatura ma minimum 37.0 stopni, dopisuje komunikat o goraczce
        if self.temperature >= 37.0:
            info += " (fever)"

        # jesli temperatura ma minimum 41.0 stopni, dopisuje dodatkowo ostrzezenie krytyczne
        if self.temperature >= 41.0:
            info += " CRITICAL TEMPERATURE!!"

        print(info)
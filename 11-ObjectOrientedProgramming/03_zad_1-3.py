# klasa TaxiRide - moj szablon do tworzenia konkretnych przejazdow taksowka
class TaxiRide:
    # konstruktor __init__ - odpala sie sam jak tworze nowy przejazd
    # self oznacza ten jeden konkretny przejazd ktory akurat tworze
    def __init__(self, rate_per_km):
        # to sa atrybuty (cechy obiektu) - zmienne przypisane do tego konkretnego kursu
        self.rate_per_km = rate_per_km  # atrybut ze stawka za 1 km (podaje ja przy tworzeniu obiektu)
        self.distance = 0               # atrybut z dystansem (na starcie 0 km)
        self.fare = 0                   # atrybut z kwota do zaplaty (na starcie 0 euro)

    # to jest metoda (czyli funkcja siedzaca w klasie) - liczy ile wyjdzie za przejazd
    def calculate_fare(self, distance):
        self.distance = distance                        # zapisuje podany dystans do atrybutu distance
        self.fare = self.distance * self.rate_per_km    # licze koszt kursu i zapisuje wynik w atrybucie fare

    # moja nowa metoda - wyciaga zapisane atrybuty i drukuje z nich paragon
    def print_receipt(self):
        print("--- RECEIPT ---")
        print(f"Distance: {self.distance} km")      # wypisuje dystans z atrybutu self.distance
        print(f"Rate: €{self.rate_per_km}/km")      # wypisuje stawke z atrybutu self.rate_per_km
        print(f"Fare: €{self.fare}")                # wypisuje wyliczona cene z atrybutu self.fare
        print("---------------")


# glowna funkcja programu
def main():
    # tworze dwa obiekty (konkretne przejazdy na bazie szablonu klasy TaxiRide)
    ride1 = TaxiRide(2)  # obiekt ride1 - pierwszy przejazd ze stawka 2 euro/km
    ride2 = TaxiRide(3)  # obiekt ride2 - drugi przejazd ze stawka 3 euro/km

    # wywoluje (odpalam) metode calculate_fare dla kazdego obiektu z osobna
    ride1.calculate_fare(10)  # licze oplate dla ride1 za 10 km (wyjdzie 20)
    ride2.calculate_fare(15)  # licze oplate dla ride2 za 15 km (wyjdzie 45)

    # wywoluje metode print_receipt na obu obiektach zeby wydrukowac paragony
    ride1.print_receipt()
    ride2.print_receipt()


# standardowy warunek - odpala funkcje main jak uruchamiam ten plik
if __name__ == "__main__":
    main()
# klasa Phone - moj szablon opisujacy smartfona (jego stany i zachowania)
class Phone():
    # konstruktor __init__ - odpala sie sam jak tworze nowy telefon
    # self oznacza ten jeden konkretny telefon ktory akurat tworze
    def __init__(self, brand, model, battery):
        # to sa atrybuty (stany / cechy obiektu) - zmienne przypisane do tego konkretnego telefonu
        self.brand = brand        # atrybut z marka telefonu
        self.model = model        # atrybut z modelem telefonu
        self.battery = battery    # atrybut z poziomem baterii w procentach
        self.is_locked = True     # atrybut logiczny czy ekran jest zablokowany (na starcie tak)

    # to jest metoda (czyli funkcja siedzaca w klasie) - odblokowuje ekran telefonu
    def unlock(self):
        self.is_locked = False
        print("Telefon zostal odblokowany.")

    # metoda blokujaca ekran telefonu
    def lock(self):
        self.is_locked = True
        print("Telefon zostal zablokowany.")

    # metoda ladujaca baterie o podana liczbe procentow (ale maks do 100%)
    def charge(self, percent):
        self.battery = min(100, self.battery + percent)
        print(f"Naladowano baterie. Aktualny poziom: {self.battery}%")

    # metoda wykonujaca polaczenie jesli telefon jest odblokowany i ma baterie
    def call(self, contact):
        if not self.is_locked and self.battery > 0:
            print(f"Dzwonie do: {contact}...")
            self.battery -= 2  # rozmowa zabiera 2% baterii z atrybutu self.battery
        else:
            print("Nie mozna zadzwonic - odblokuj najpierw telefon lub naladuj baterie.")

    # metoda wyciagajaca zapisane atrybuty i wyswietlajaca wszystkie wlasciwosci telefonu
    def display_properties(self):
        print("--- PHONE PROPERTIES ---")
        print(f"Brand: {self.brand}")          # wypisuje marke z atrybutu self.brand
        print(f"Model: {self.model}")          # wypisuje model z atrybutu self.model
        print(f"Battery: {self.battery}%")     # wypisuje stan baterii z atrybutu self.battery
        print(f"Is locked: {self.is_locked}")  # wypisuje stan blokady z atrybutu self.is_locked
        print("------------------------")


# glowna funkcja programu
def main():
    # tworze obiekt my_phone (konkretny smartfon na bazie szablonu klasy Phone)
    my_phone = Phone("Apple", "iPhone 15 Pro Max", 65)

    # wywoluje (odpalam) metody na obiekcie my_phone (zachowania telefonu)
    my_phone.unlock()
    my_phone.call("Nikola")
    my_phone.charge(20)
    my_phone.lock()

    # wyswietlam wszystkie aktualne wlasciwosci (atrybuty) obiektu my_phone
    my_phone.display_properties()


# standardowy warunek - odpala funkcje main jak uruchamiam ten plik
if __name__ == "__main__":
    main()
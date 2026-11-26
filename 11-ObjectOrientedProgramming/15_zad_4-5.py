# importuje klase Thermometer z mojego drugiego pliku thermometer.py
from thermometer import Thermometer


# glowna funkcja programu
def main():
    # 1. tworze obiekt my_thermometer (konkretny termometr na bazie szablonu z pliku thermometer.py)
    my_thermometer = Thermometer()

    # wywoluje (odpalam) metody po kolei zgodnie z punktami w zadaniu
    my_thermometer.turn_on()   # 2. wlaczam termometr
    my_thermometer.measure()   # 3. mierze temperature (losuje wynik)
    my_thermometer.display()   # 4. wyswietlam temperature na ekranie
    my_thermometer.turn_off()  # 5. wylaczam termometr


# standardowy warunek - odpala funkcje main jak uruchamiam ten plik
if __name__ == "__main__":
    main()
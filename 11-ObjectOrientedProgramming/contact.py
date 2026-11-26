# klasa Contact - moj szablon pojedynczego kontaktu na smartfonie
class Contact:
    # konstruktor __init__ - odpala sie sam jak tworze nowy kontakt
    # self oznacza ten jeden konkretny kontakt ktory akurat tworze
    def __init__(self, name, email, telephone):
        # to sa atrybuty (cechy obiektu) - dane przypisane do tego kontaktu
        self.name = name            # atrybut z imieniem i nazwiskiem
        self.email = email          # atrybut z adresem e-mail
        self.telephone = telephone  # atrybut z numerem telefonu

    # metoda specjalna __str__ - mowi Pythonowi jak zamienic obiekt kontaktu na tekst w print()
    # :<15 oraz :<20 wyrownuja napisy w rownych kolumnach tak jak na przykladzie w zadaniu
    def __str__(self):
        return f"{self.name:<15} {self.email:<20} {self.telephone}"
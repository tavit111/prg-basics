# klasa Contact_List - moj szablon listy kontaktow przechowujacej obiekty klasy Contact
class Contact_List:
    # konstruktor __init__ - odpala sie sam jak tworze nowa liste kontaktow
    def __init__(self):
        # atrybut (cecha obiektu) - pusta lista na obiekty pojedynczych kontaktow
        self.contacts = []

    # to jest metoda (czyli funkcja siedzaca w klasie) - dorzuca obiekt kontaktu na liste
    def add_contact(self, contact):
        self.contacts.append(contact)

    # metoda przechodzaca po calej liscie self.contacts i drukujaca kazdy kontakt po kolei
    def display_contacts(self):
        for contact in self.contacts:
            # print() sam odpala w tle metode __str__() z klasy Contact
            print(contact)
# importuje obie klasy z moich dwoch pozostalych plikow (bez dopisywania .py)
from contact import Contact
from contact_list import Contact_List


# glowna funkcja programu
def main():
    # tworze obiekt my_contacts (konkretna lista kontaktow na bazie klasy Contact_List)
    my_contacts = Contact_List()

    # tworze 4 obiekty pojedynczych kontaktow (z klasy Contact) i wrzucam je na liste
    my_contacts.add_contact(Contact("John Brown", "brown@onet.pl", "555234000"))
    my_contacts.add_contact(Contact("Anna May", "am@o2.pl", "232000199"))
    my_contacts.add_contact(Contact("George Small", "smallg@google.pl", "222999100"))
    my_contacts.add_contact(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

    # wyswietlam cala liste kontaktow zapisana na smartfonie
    my_contacts.display_contacts()


# standardowy warunek - odpala funkcje main jak uruchamiam ten plik
if __name__ == "__main__":
    main()
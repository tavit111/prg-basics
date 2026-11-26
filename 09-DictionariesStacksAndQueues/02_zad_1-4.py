# tworze slownik z danymi osoby
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}

# wyswietlam imie, hobby i caly slownik przed zmianami
print(person["name"])
print(person["hobby"])
print(person)

# zmieniam nazwisko na Nowak i odwracam status malzenski
person["surname"] = "Nowak"
person["married"] = not person["married"]

# dodaje plec, dopisuje nowe hobby do listy i dodaje telefon sluzbowy
person["gender"] = "mężczyzna"
person["hobby"].append("rower")
person["phone"]["work"] = "313131444"

# wyswietlam caly zaktualizowany slownik za pomoca petli
for key, value in person.items():
    print(f"{key}: {value}")
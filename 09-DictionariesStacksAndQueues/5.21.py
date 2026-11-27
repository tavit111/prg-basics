import json

# Słownik opisujący książkę "Mistrz i Małgorzata" (co najmniej 5 par klucz-wartość)
favourite_book = {
    'title': 'Mistrz i Małgorzata',
    'author': 'Michaił Bułhakow',
    'publication_year': 1967,
    'genre': ['powieść fantastyczna', 'satyra', 'realizm magiczny'],
    'setting': ['Moskwa (lata 30. XX w.)', 'Jeruzalem (czasy Poncjusza Piłata)'],
    'main_characters': [
        'Mistrz',
        'Małgorzata',
        'Woland',
        'Behemot',
        'Poncjusz Piłat',
    ],
    'is_classic': True,
}

# Zapisanie słownika do pliku favourite.json
with open('favourite.json', 'w', encoding='utf-8') as file:
  json.dump(favourite_book, file, indent=4, ensure_ascii=False) #Dzięki tym parametrom polskie litery w tytule, nazwisku autora i nazwach bohaterów zostaną zapisane w pliku czytelnie, a nie w postaci kodów Unicode

print('Dane zostały zapisane do pliku favourite.json.')

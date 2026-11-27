import json

# Otwarcie pliku dogs.json w trybie odczytu
with open('dogs.json', 'r', encoding='utf-8') as file:
  dogs = json.load(file)

# Przejście przez listę psów i wyświetlenie tych młodszych niż 5 lat
for dog in dogs:
  if dog['age'] < 5:
    for key, value in dog.items():
      print(key, ':', value)
    print()

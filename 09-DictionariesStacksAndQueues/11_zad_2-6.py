# zbiory z wymaganymi uprawnieniami i uprawnieniami uzytkownika
required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

# sprawdzam, czy wymagane uprawnienia sa podzbiorem uprawnien uzytkownika
has_permissions = required_permissions.issubset(user_permissions)

# wypisuje wynik (zwroci False, bo brakuje "execute")
print(has_permissions)
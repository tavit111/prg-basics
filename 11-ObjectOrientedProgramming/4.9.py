class C:

  def __init__(self, name, surname, age, seniority):
    self.name = name
    self.surname = surname
    self.age = age
    self.seniority = seniority

  def __str__(self):
    text = f"{self.surname}{self.name[0]}{self.seniority}"
    if self.age >= 18:
      return text.upper()
    else:
      return text.lower()


def main():
  employee1 = C("Anna", "May", 17, 7) #obiekt
  employee2 = C("George", "Brown", 21, 4) #obiekt

  print(employee1)  # maya7
  print(employee2)  # BROWNG4


if __name__ == "__main__":
  main()

def reverse_string(text):
  stack = []

  # Wrzucenie każdego znaku na stos (push)
  for char in text:
    stack.append(char)

  reversed_text = ''

  # Zdejmowanie znaków ze stosu (pop) w odwrotnej kolejności
  while stack:
    reversed_text += stack.pop()

  return reversed_text


# Pobranie tekstu od użytkownika i wyświetlenie odwróconego wyniku
user_text = input('Enter text to reverse: ')
print('Reversed text:', reverse_string(user_text))

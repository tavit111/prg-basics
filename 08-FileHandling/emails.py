import re


def _read_email(file_name='email.txt'):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


def email_sender():
    content = _read_email()
    match = re.search(r'^From:.*?([\w.-]+@[\w.-]+\.\w+)', content, re.MULTILINE) #content – tekst (zawartość pliku email.txt), w którym funkcja szuka dopasowania#dzięki fladze re.MULTILINE znak ^ dopasowuje początek każdej linii, a nie tylko całego pliku
    return match.group(1) if match else None #match.group()) – zwraca cały dopasowany fragment tekstu, łącznie z nagłówkiem czy spacjami.
                                             #match.group(1) - zwróci samo 'Spotkanie'

def email_recipient():
    content = _read_email()
    match = re.search(r'^To:.*?([\w.-]+@[\w.-]+\.\w+)', content, re.MULTILINE)
    return match.group(1) if match else None


def email_subject():
    content = _read_email()
    match = re.search(r'^Subject:\s*(.+)', content, re.MULTILINE)
    return match.group(1) if match else None


def email_body():
    content = _read_email()
    match = re.search(r'\r?\n\r?\n(.*)', content, re.DOTALL) #Flaga re.DOTALL sprawia, że kropka . dopasowuje również znaki nowej linii, dzięki czemu .* pobiera całą wielowierszową treść wiadomości.
    return match.group(1).strip() if match else None

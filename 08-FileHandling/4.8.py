import re

file_name = 'files.txt'
pattern = r'^.+\.[A-Za-z0-9]{4}$'

with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if re.match(pattern, line): #porównuje początek i całość napisu line ze wzorcem
            print(line)

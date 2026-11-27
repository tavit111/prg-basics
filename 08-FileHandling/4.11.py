file_name = 'powers.txt'

with open(file_name, 'w', encoding='utf-8') as file:
    for number in range(1, 101):
        line = f'{number},{number**2},{number**3}'
        print(line)
        file.write(line + '\n')

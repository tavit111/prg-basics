# nazwy plikow - zrodlowego i wynikowego
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# stanowisko, ktorego szukamy
job_title = 'Software Engineer'

# otwieram plik z pracownikami do odczytu i nowy plik do zapisu
with open(employees_file, 'r') as source_file:
    with open(position_file, 'w') as target_file:
        # przechodze po kolei przez kazda linijke z pliku zrodlowego
        for line in source_file:
            # jesli w linijce jest szukane stanowisko, zapisuje ja do drugiego pliku
            if job_title in line:
                target_file.write(line)
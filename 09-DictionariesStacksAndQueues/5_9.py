###
# Counts vehicles registered in each Polish province
#
import csv

provinces = {}
vehicles_count = {}

# Read province codes from CSV file
with open('province.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    for row in reader:
        letter = row[0]
        province = row[1]

        provinces[letter] = province
        vehicles_count[province] = 0

# Read vehicle registration numbers
with open('vehicle.txt', 'r', encoding='utf-8') as file:
    for line in file:
        registration = line.strip()

        if registration:
            letter = registration[0]

            if letter in provinces:
                province = provinces[letter]
                vehicles_count[province] += 1

# Print results
print("VEHICLES BY PROVINCE")
print("--------------------")

for province, count in vehicles_count.items():
    print(f"{province}: {count}")
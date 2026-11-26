###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    for id, line in enumerate(file, start=1):
        print(f"{id}. {line}", end="")

print()
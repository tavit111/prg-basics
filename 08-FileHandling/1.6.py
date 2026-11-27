###
# Reads the entire contents of a file
#
def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read() #odczytuje całą zawartość pliku naraz i zapisuje ją jako jeden długi ciąg znaków (tekst typu str) w zmiennej content.
    return content

# reads the entire file
file_content = read_from_file('countries.txt') #cała zawartość pliku jako jeden string trafia do zmiennej

# splits the entire file contents into lines
# and stores them in an array
file_lines = file_content.splitlines() # tnie ten tekst w miejscach występowania znaków nowej linii (\n)

sorted_lines = sorted(file_lines) #sorts the array alphabetically

# prints the array
for line in sorted_lines:
    print(line)

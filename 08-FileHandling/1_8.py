###
# Reads text from a file and counts the number of words
#
word_count = 0

with open('pets.txt', 'r') as file:
    for line in file:
        print(line, end="")
        word_count += len(line.split())

print()
print("Number of words:", word_count)
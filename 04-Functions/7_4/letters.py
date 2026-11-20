###
# Counts how many times a given letter appears in a text
#
def count_letter(text, letter):
    count = 0

    for char in text:
        if char == letter:
            count += 1

    return count
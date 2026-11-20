###
# Spells out a name using the ICAO phonetic alphabet
#
def icao(letter):
    if letter == 'A':
        return 'Alfa'
    elif letter == 'B':
        return 'Bravo'
    elif letter == 'C':
        return 'Charlie'
    elif letter == 'D':
        return 'Delta'
    elif letter == 'E':
        return 'Echo'
    elif letter == 'F':
        return 'Foxtrot'
    elif letter == 'G':
        return 'Golf'
    elif letter == 'H':
        return 'Hotel'
    elif letter == 'I':
        return 'India'
    elif letter == 'J':
        return 'Juliett'
    elif letter == 'K':
        return 'Kilo'
    elif letter == 'L':
        return 'Lima'
    elif letter == 'M':
        return 'Mike'
    elif letter == 'N':
        return 'November'
    elif letter == 'O':
        return 'Oscar'
    elif letter == 'P':
        return 'Papa'
    elif letter == 'Q':
        return 'Quebec'
    elif letter == 'R':
        return 'Romeo'
    elif letter == 'S':
        return 'Sierra'
    elif letter == 'T':
        return 'Tango'
    elif letter == 'U':
        return 'Uniform'
    elif letter == 'V':
        return 'Victor'
    elif letter == 'W':
        return 'Whiskey'
    elif letter == 'X':
        return 'X-ray'
    elif letter == 'Y':
        return 'Yankee'
    elif letter == 'Z':
        return 'Zulu'
    else:
        return ''

name = input('Enter name: ')

for letter in name.upper():
    print(icao(letter), end=' \n')
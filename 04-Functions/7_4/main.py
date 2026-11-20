###
# Counts occurrences of the letter 'e' in a text
#
import letters

def main():
    text = "You never get a second chance to make a first impression"
    letter = 'e'

    print(text)
    print(f"The number of letter '{letter}': {letters.count_letter(text, letter)}")


if __name__ == "__main__":
    main()
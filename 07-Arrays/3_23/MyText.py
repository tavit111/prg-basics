###
# Functions for operating on text
#

# Returns the number of words in the text
def word_count(text):
    return len(text.split())


# Returns words sorted from longest to shortest
def longest_words(text):
    words = text.split()
    return sorted(words, key=len, reverse=True)


# Returns words sorted alphabetically
def alphabetical_words(text):
    words = text.split()
    return sorted(words)
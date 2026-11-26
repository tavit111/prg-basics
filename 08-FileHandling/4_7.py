###
# Counts vowels in a text using regular expressions
#
import re

text = input("Enter text: ")

pattern = r'[aeiou]'

vowels = re.findall(pattern, text, re.IGNORECASE)

print("Number of vowels:", len(vowels))
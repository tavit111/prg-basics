###
# Tests functions from MyText module
#
import MyText

text = "An apple a day keeps the doctor away"

print("Text:", text)
print("Number of words:", MyText.word_count(text))
print("Words from the longest:", ",".join(MyText.longest_words(text)))
print("Words ordered alphabetically:", ",".join(MyText.alphabetical_words(text)))
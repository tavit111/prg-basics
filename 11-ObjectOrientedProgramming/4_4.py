###
# Tests the E-book class
# - Create an e-book
# - Open the book
# - Display its status
# - Read a few pages
# - Display its updated status
# - Close the book
# - Try reading while the book is closed
#
import ebook


# Object creation
my_book = ebook.Ebook(
    "Harry Potter and the Philosopher's Stone",
    "J. K. Rowling",
    223
)

# Open the book
my_book.open()

# Display book status
my_book.show_status()

# Read a few pages
my_book.next_page()
my_book.next_page()
my_book.next_page()
my_book.previous_page()

# Display updated book status
print()
my_book.show_status()

# Close the book
my_book.close()

# Try reading while the book is closed
print()
my_book.next_page()
my_book.previous_page()

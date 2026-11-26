###
# Calculates the total value of money spent
#
import re  # Module for regular expressions

# File name with shopping report
email_file = 'report.txt'

# Read the content of email
with open(email_file, 'r', encoding='utf-8') as file:
    email = file.read()

# Regular expression pattern for amounts
pattern = r'€(\d+)'

# Extract numbers from email
amounts = re.findall(pattern, email)

# Calculate the total purchases
total = 0

for amount in amounts:
    total += int(amount)

# Print result
print(f"Total money spent: €{total}")
###
# Finds the most expensive expense category
#

# the list of categorise and thier corresponding expenses
categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense = max(expenses)
max_index = expenses.index(max_expense)

print("Most expensive category:", categories[max_index])
print("Amount:", max_expense)
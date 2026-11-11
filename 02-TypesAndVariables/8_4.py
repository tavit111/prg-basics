###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170

total_inches = round(cm / 2.54)

# Calculate the number of feet
feet = total_inches // 12
print(total_inches / 12)
print(feet)

# Calculate the remaining inches
inches = total_inches % 12

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
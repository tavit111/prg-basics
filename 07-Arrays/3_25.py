###
# Draws the graph of f(x) = x² - 3
# Activate the envirement: source .venv/bin/activate
#
import matplotlib.pyplot as plt

x = []
y = []

# Create x values
for n in range(-100, 101):
    x = x + [n]

# Create y values
for n in x:
    y = y + [n ** 2 - 3]

# Print chart
plt.plot(x, y)
plt.show()
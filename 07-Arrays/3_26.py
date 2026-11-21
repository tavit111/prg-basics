###
# Draws the graph of y = sin(x)
# Activate the envirement: source .venv/bin/activate
#
import matplotlib.pyplot as plt
import math

x = []
y = []

# Create x values (degrees)
for n in range(0, 361):
    x.append(n)

# Create y values
for n in x:
    y.append(math.sin(math.radians(n)))

# Print chart
plt.plot(x, y)
plt.show()
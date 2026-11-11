###
# A program that reads temperature in degrees Celsius
# and converts it to Kelvin and Fahrenheit.
#

# Read temperature in Celsius
celsius = int(input('Enter temperature in Celsius: '))

# Calculate temperature in Kelvin
kelvin = celsius + 273.15

# Calculate temperature in Fahrenheit
fahrenheit = celsius * 9 / 5 + 32

# Print results
print(f'Temperature in Kelvin: {kelvin:.2f}')
print(f'Temperature in Fahrenheit: {fahrenheit:.2f}')
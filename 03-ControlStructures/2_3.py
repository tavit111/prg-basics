###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# The average fuel consumption per 100 km is 7, 9 and 6 liters.
# A program that calculates total fuel consumption.
#
driving_mode = input('Enter driving mode (A/M/E): ')
distance = int(input('Enter distance in km: '))

if driving_mode == 'A':
    fuel_consumption = 7  # liters per 100 km
elif driving_mode == 'M':
    fuel_consumption = 9
elif driving_mode == 'E':
    fuel_consumption = 6
else:
    fuel_consumption = 0
    print('Incorrect driving mode')

total_consumption = distance * fuel_consumption / 100

print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')
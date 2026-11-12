###
# Converts time from 24-hour format to 12-hour format
#
time = input("Enter time (24-hour format): ")

hour, minutes = time.split(':')
hour = int(hour)

if hour >= 12:
    period = "pm"
else:
    period = "am"

if hour == 0:
    hour = 12
elif hour > 12:
    hour -= 12

print(f"Time in 12-hour format: {hour}:{minutes}{period}")
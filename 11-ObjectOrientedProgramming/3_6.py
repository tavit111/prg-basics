###
# Task 6: Tests TV volume control
# - Create TV and display initial volume (0)
# - Turn TV on
# - Increase and decrease volume
# - Verify maximum volume limit (10)
# - Verify minimum volume limit (0)
#
import tv


# Object creation
my_tv = tv.TV()

my_tv.show_status()

my_tv.turn_on()
my_tv.show_status()

# Increase volume to 3
my_tv.increase_volume()
my_tv.increase_volume()
my_tv.increase_volume()
my_tv.show_status()

# Decrease volume to 2
my_tv.decrease_volume()
my_tv.show_status()

# Try increasing volume beyond maximum (10)
for i in range(15):
    my_tv.increase_volume()

my_tv.show_status()

# Try decreasing volume below minimum (0)
for i in range(15):
    my_tv.decrease_volume()

my_tv.show_status()

my_tv.turn_off()
my_tv.show_status()

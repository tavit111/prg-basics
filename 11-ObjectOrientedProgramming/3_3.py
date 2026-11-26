###
# Task 3: Tests changing TV channels
# - Create TV and display status
# - Turn TV on
# - Change channel to 5
# - Display updated channel number
# - Turn TV off and display status
#
import tv



# Object creation
my_tv = tv.TV()

# Object usage
my_tv.show_status()

my_tv.turn_on()
my_tv.show_status()

my_tv.set_channel(5)
my_tv.show_status()

my_tv.turn_off()
my_tv.show_status()

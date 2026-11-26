###
# Task 4: Tests the list of available TV channels
# - Create TV and display status
# - Turn TV on
# - Display initially empty channel list
# - Program six TV channels
# - Display numbered channel list
# - Display TV status and turn TV off
#
import tv


# Object creation
my_tv = tv.TV()

# Object usage
my_tv.show_status()

my_tv.turn_on()
my_tv.show_status()

my_tv.show_channels()

my_tv.set_channels([
    "TVP1",
    "TVP2",
    "Polsat",
    "TVN",
    "Filmbox",
    "Discovery"
])

my_tv.show_channels()

my_tv.show_status()

my_tv.turn_off()


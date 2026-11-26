###
# Task 5: Tests displaying TV channel names
# - Create TV and program seven channels
# - Turn TV on
# - Display channel 1 with its name
# - Change to channels 4 and 7
# - Change to unavailable channel 9
# - Verify that unavailable channels have no name displayed
#
import tv


# Object creation
my_tv = tv.TV()

# Set seven available channels
my_tv.set_channels([
    "TVP1",
    "TVP2",
    "Polsat",
    "TVN",
    "Filmbox",
    "Discovery",
    "National Geographic"
])

my_tv.turn_on()
my_tv.show_status()

# Change channel to 4
my_tv.set_channel(4)
my_tv.show_status()

# Change channel to 7
my_tv.set_channel(7)
my_tv.show_status()

# Change to an unavailable channel
my_tv.set_channel(9)
my_tv.show_status()

my_tv.turn_off()

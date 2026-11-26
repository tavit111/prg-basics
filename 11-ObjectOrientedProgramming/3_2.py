###
# Tests the current channel number
# - Verify that the initial channel is 1
# - Display the channel when TV is on
# - Verify that the channel is hidden when TV is off
#
import tv


# Object creation
my_tv = tv.TV()

# TV initially off
my_tv.show_status()

# TV turned on
my_tv.turn_on()
my_tv.show_status()

# TV turned off
my_tv.turn_off()
my_tv.show_status()

###
# Tests TV  class operations
# - Create a TV object
# - Display initial status
# - Turn TV on and display status
# - Turn TV off and display status
#

import tv

# Object creation
my_tv = tv.TV()

# Object usage
my_tv.show_status()

my_tv.turn_on()
my_tv.show_status()

my_tv.turn_off()
my_tv.show_status()


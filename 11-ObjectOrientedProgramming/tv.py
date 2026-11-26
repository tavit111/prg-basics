###
# Complete TV class with features from tasks 1-6
#

class TV:
    def __init__(self):
        # Task 1: TV power status
        self.is_on = False

        # Task 2: Current channel number
        self.channel_no = 1

        # Task 4: List of available channels
        self.channels = []

        # Task 6: Volume level (0-10)
        self.volume = 0

    # Task 1: Turn TV on
    def turn_on(self):
        self.is_on = True

    # Task 1: Turn TV off
    def turn_off(self):
        self.is_on = False

    # Task 3: Change current channel number
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    # Task 4: Set available channels
    def set_channels(self, channels_list):
        self.channels = channels_list

    # Task 4: Display available channels
    def show_channels(self):
        print("Channel list:")

        for i, channel in enumerate(self.channels, start=1):
            print(f"{i}. {channel}")

    # Task 6: Increase volume by one
    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1

    # Task 6: Decrease volume by one
    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    # Tasks 1, 2, 5, 6: Display TV status
    def show_status(self):
        if self.is_on:
            status = f"TV is on, channel {self.channel_no}"

            # Task 5: Display channel name if available
            if 1 <= self.channel_no <= len(self.channels):
                channel_name = self.channels[self.channel_no - 1]
                status += f" ({channel_name})"

            # Task 6: Display volume level
            status += f", volume {self.volume}"

            print(status)

        else:
            print(f"TV is off, volume {self.volume}")
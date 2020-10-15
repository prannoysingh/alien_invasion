class Settings:
    """A class to sore all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,230)
        # self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 50
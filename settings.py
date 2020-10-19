class Settings:
    """A class to sore all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # self.bg_color = (0,0,230)

        # Ship settings
        self.ship_speed = 50

        # Bullet settings
        self.bullet_speed = 20.0
        self.bullet_width = 30
        self.bullet_height = 25
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10000

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
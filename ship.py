import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set it's starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image and get its rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # self.rect.midbottom = self.screen_rect.center

        # Store a horizontal value for a ships horizontal position.
        self.x = float(self.rect.x)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Move the ship to right if the flag is true.
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            # Move the ship to left if the flag is true.
            self.rect.x -= self.settings.ship_speed

    def blitme(self):
        """Draw ship at the current location"""
        self.screen.blit(self.image, self.rect)
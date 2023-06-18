"""
This module includes the Ship class, used for managing the ship's behavior in the game.

Class:
    - Ship: A class to manage the ship.

Methods in Ship:
    - __init__: Initializes the ship and sets its starting position.
    - update: Updates the ship's position based on the movement flags.
    - blitme: Draws the ship at its current location.
    - center_ship: Centers the ship on the screen.

Attributes in Ship:
    - screen, settings, screen_rect: Contains information about the game screen and settings.
    - image, rect: Related to the ship's image and position.
    - x: Stores a float value for the ship's exact horizontal position.
    - moving_right, moving_left: Movement flags for the ship's direction.

By importing this module and creating an instance of Ship, one can manage the ship's appearance, position, and movement
within the game.
"""


import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

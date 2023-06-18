"""
This module includes the Alien class, used for representing a single alien in the game's fleet.

Class:
    - Alien: A class to represent a single alien in the fleet.

Methods in Alien:
    - __init__: Initializes the alien and sets its starting position.
    - check_edges: Returns True if the alien is at the edge of the screen.
    - update: Moves the alien right or left.

Attributes in Alien:
    - screen, settings: Contains information about the game screen and settings.
    - image, rect: Related to the alien's image and position.
    - x: Stores a float value for the alien's exact horizontal position.

By importing this module and creating instances of Alien, one can manage the aliens' appearances,
positions, and movements within the game.
"""


import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horrizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

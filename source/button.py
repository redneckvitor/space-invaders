"""
This module contains the Button class, which is used to create interactive buttons in the game interface.

Class:
    - Button: A class to create and manage interactive buttons.

Methods in Button:
    - __init__: Initializes button by setting its position, size, and text attributes.
    - draw_button: Draws the button and the text onto the screen.
    - prep_msg: Turn msg into a rendered image and center text on the button.

Attributes in Button:
    - msg_image, msg_image_rect: Information about the message to be displayed on the button.
    - rect, screen, screen_rect: Information about the button and screen dimensions.
    - button_color, text_color: Color specifications for the button and the text.
    - font: Specifies the font used for the text on the button.

This module handles the creation, placement, and display of interactive buttons in the game.
"""


import pygame.font


class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

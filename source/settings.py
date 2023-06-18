"""
This module contains the Settings class, which is used to store all settings for the game.

Class:
    - Settings: A class to store all settings for the game.

Methods in Settings:
    - __init__: Initializes the game's static settings.
    - initialize_dynamic_settings: Initialize settings that change throughout the game.
    - increase_speed: Increase speed settings and alien point values.

Attributes in Settings:
    - screen_width, screen_height, bg_color: Screen settings.
    - ship_speed, ship_limit: Ship settings.
    - bullet_speed, bullet_width, bullet_height, bullet_color, bullets_allowed: Bullet settings.
    - alien_speed, fleet_drop_speed, fleet_direction: Alien settings.
    - speedup_scale, score_scale: Game speedup and scoring settings.
    - other attributes to manage dynamic game settings.

By importing this module and creating an instance of Settings, one can easily manage and adjust game settings.
"""


class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initializes game's static settings."""

        # Screen settings
        self.screen_width = 1200    # Default: 1200
        self.screen_height = 800    # Default: 800
        self.bg_color = (230, 230, 230)   # Default: (230, 230, 230)

        # Ship settings
        self.ship_speed = 4.5   # Default: 4.5
        self.ship_limit = 3   # Default: 3

        # Bullet settings
        self.bullet_speed = 220.0   # Default: 220.0
        self.bullet_width = 5   # Default: 5
        self.bullet_height = 40   # Default: 40
        self.bullet_color = (255, 60, 60)   # Default: (255, 60, 60)
        self.bullets_allowed = 4    # Default: 4

        # Alien settings
        self.alien_speed = 8.0   # Default: 10.0
        self.fleet_drop_speed = 50   # Default: 50

        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1    # Default: 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1    # Default: 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5   # Default: 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 8.0
        self.bullet_speed = 10.0
        self.alien_speed = 2.0

        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points + self.score_scale)

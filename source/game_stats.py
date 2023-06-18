"""
This module contains the GameStats class, which is responsible for tracking and managing the game statistics.

Class:
    - GameStats: A class to track game statistics.

Methods in GameStats:
    - __init__: Initializes the game's statistics and settings.
    - reset_stats: Resets the game statistics that can change during the game.

Attributes in GameStats:
    - settings: Game settings.
    - high_score: The highest score achieved in the game.
    - ships_left: Number of remaining ships.
    - score: Current score.
    - level: Current level.

This module handles the tracking and management of game statistics, such as the high score, remaining ships, current score, and level.
"""


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

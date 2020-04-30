class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, pong_game):
        """Initialize statistics."""
        self.settings = pong_game.settings
        # self.reset_stats()

        self.game_active = True


    # def reset_stats(self):
    #     """Initialize statistics that can change during the game."""
    #     self.ships_left = self.settings.ship_limit
class GameStats:
    """Track statistics for Pong."""
    def __init__(self, pong_game):
        """Initialize statistics."""
        self.settings = pong_game.settings
        self.reset_stats()

        self.rally_length = 0

        # Start game in inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        print("stats reset")
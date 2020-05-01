import pygame.font

class Scoreboard:
    """A class to report scoring information."""
    
    def __init__(self, pong_game):
        """Initialize scorekeeping attributes."""
        self.screen = pong_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = pong_game.settings
        self.stats = pong_game.stats
        
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score image.
        self.prep_score()
        self.game_over_image = self.font.render("GAME OVER", True,
                self.text_color, self.settings.bg_color)

        self.game_over_rect = self.score_image.get_rect()
        self.game_over_rect.center = self.screen_rect.center
        self.game_over_rect.top = 100
    
    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)
                
        self.score_rect = self.score_image.get_rect()
        self.score_rect.center = self.screen_rect.center
        self.score_rect.top = 20
            
    # def game_over(self):
    #     self.score_image = self.font.render("game over", True,
    #             self.text_color, self.settings.bg_color)
                
    #     self.score_rect = self.score_image.get_rect()
    #     self.score_rect.center = self.screen_rect.center
    #     self.score_rect.top = 50

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        if self.stats.score[0] >= 2 or self.stats.score[1] >= 2:
            self.screen.blit(self.game_over_image, self.game_over_rect)
            


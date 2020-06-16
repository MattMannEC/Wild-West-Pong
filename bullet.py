import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, pong_game, paddle):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = pong_game.screen
        self.settings = pong_game.settings
        self.color = self.settings.bullet_color

        # Paddle object tells bullet which paddle it was fired by, determining
        # x_trajectory and rect
        self.paddle = paddle

        self.rect = pygame.Rect(0, 0, 
            (self.settings.bullet_width * pong_game.relative_unit), 
            (self.settings.bullet_height * pong_game.relative_unit))
        
        # Bullets fired from left_paddle have an x velocity of 1
        if self.paddle.position == 'left':
            self.rect.center = pong_game.left_paddle.rect.center
            self.x_trajectory = (1 * pong_game.relative_unit)        
            
        # Bullets fired from left_paddle have an x velocity of -1
        elif self.paddle.position == 'right':
            self.rect.center = pong_game.right_paddle.rect.center
            self.x_trajectory = (-1 * pong_game.relative_unit)

        self.x = float(self.rect.x)
    
    def update(self, pong_game):
        self.x += (self.settings.bullet_speed * pong_game.relative_unit) * self.x_trajectory
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
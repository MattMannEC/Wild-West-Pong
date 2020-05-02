import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, pong_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = pong_game.screen
        self.settings = pong_game.settings
        self.color = self.settings.bullet_color

        # Create bullet
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self.rect.midtop = pong_game.left_paddle.rect.midtop

        self.x = float(self.rect.x)
    
    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
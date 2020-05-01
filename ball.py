import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):

    def __init__(self, pong_game):
        super().__init__()
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = pong_game.settings

        self.rect = pygame.Rect(self.screen_rect.centerx, self.screen_rect.centery, self.settings.ball_width, self.settings.ball_height)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # X axis is randomly -1 or 1
        self.serve_x = (-1) ** randint(2,3)
        # Y axis is random float between 0.0 and 1.0 either positive or negative
        self.serve_y = ((randint(5, 10)/10) * -1) ** randint(2,3)

        self.settings.velocity = [self.serve_x, self.serve_y]


    def update(self):
        # Update x axis position
        self.x += self.settings.velocity[0]
        self.rect.x = self.x

        # Update y axis position
        self.y += self.settings.velocity[1]
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.ball_color, self.rect)


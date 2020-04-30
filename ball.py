import pygame
from pygame.sprite import Sprite
from random import *

class Ball(Sprite):

    def __init__(self, pong_game):
        super().__init__()
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = pong_game.settings

        self.rect = pygame.Rect(self.screen_rect.centerx, self.screen_rect.centery, self.settings.ball_width, self.settings.ball_height)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.y_velocity = self.settings.ball_speed 
        self.x_velocity = self.settings.ball_speed

        # Set random service direction
        self.rand_x = randint(0, 1)
        if self.rand_x == 1:
            self.x_velocity *= -1
            
        # Set random service trajectory
        self.rand_y = randint(1, 6)
        if self.rand_y == 1:
            self.y_velocity *= 1.2
        elif self.rand_y == 2:
            self.y_velocity *= 1.4
        elif self.rand_y == 3:
            self.y_velocity *= 1.6
        elif self.rand_y == 4:
            self.y_velocity *= -1.2
        elif self.rand_y == 5:
            self.y_velocity *= -1.4
        elif self.rand_y == 6:
            self.y_velocity *= -1.6
        

    def update(self):
        # Update x axis position
        self.x += self.x_velocity
        self.rect.x = self.x

        # Update y axis position
        self.y += self.y_velocity
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.ball_color, self.rect)


import pygame
from pygame.sprite import Sprite

class Ball(Sprite):

    def __init__(self, pong_game):
        super().__init__()
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = pong_game.settings

        self.rect = pygame.Rect(100, 100, self.settings.ball_width, self.settings.ball_height)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.y_velocity = self.settings.ball_speed 
        self.x_velocity = self.settings.ball_speed

        # Get center of board where ball will be drawn.
        self.rect.center = self.screen_rect.center

    def update(self):
        # Update x axis position
        self.x += self.x_velocity
        self.rect.x = self.x

        # Update y axis position
        self.y += self.y_velocity
        self.rect.y = self.y

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.settings.ball_color, self.rect)

    def bounce(self):
        self.x_velocity *= -1

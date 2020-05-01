import pygame
import settings
from pygame.sprite import Sprite

class Paddle(Sprite):

    def __init__(self, pong_game, position):
        super().__init__()
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = pong_game.settings
        self.rect = pygame.Rect(0, 0, self.settings.paddle_width, self.settings.paddle_height)
        self.position = position
        self.set_start_position()

        # Store a decimal value for the paddle's vertical position.
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def set_start_position(self):
        if self.position == 'left':
            self.rect.midleft = self.screen_rect.midleft
            self.rect.x += 50
        if self.position == 'right':
            self.rect.midright = self.screen_rect.midright
            self.rect.x -= 50

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.paddle_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.paddle_speed

        # Update modified y axis value to actual y axis position
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.paddle_color, self.rect)

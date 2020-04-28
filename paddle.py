import pygame
import settings

class Paddle:

    def __init__(self, pong_game):

        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = pong_game.settings

        self.rect = pygame.Rect(0, 0, self.settings.paddle_width, self.settings.paddle_height)
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the paddle's vertical position.
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.paddle_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.paddle_speed

        self.rect.y = self.y

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.settings.paddle_color, self.rect)

import pygame
import settings

class Paddle:

    def __init__(self, pong_game):

        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = pong_game.settings

        self.rect = pygame.Rect(0, 0, self.settings.paddle_width, self.settings.paddle_height)
        self.rect.midleft = self.screen_rect.midleft

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.settings.paddle_color, self.rect)

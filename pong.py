import sys

import pygame
from settings import Settings
from paddle import Paddle

class Pong:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # Set main surface to fullscreen mode size
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # Save the width and height of the main surface to the settings class.
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Pong")

        self.paddle = Paddle(self)

    def run_game(self):
        while True:
            self._check_events()
            self.paddle.update()
            self._update_screen()

    def _check_events(self):
        """"Listen for when user presses buttons"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_w:
            self.paddle.moving_up = True
        elif event.key == pygame.K_s:
            self.paddle.moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_w:
            self.paddle.moving_up = False
        elif event.key == pygame.K_s:
            self.paddle.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.paddle.draw_paddle()
        pygame.display.flip()

if __name__ == '__main__':
    pong = Pong()
    pong.run_game()
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

        self.left_paddle = Paddle(self, 'left')
        self.right_paddle = Paddle(self, 'right')

    def run_game(self):
        while True:
            self._check_events()
            self.left_paddle.update()
            self.right_paddle.update()
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
        # left_paddle keydown events
        if event.key == pygame.K_w:
            self.left_paddle.moving_up = True
        elif event.key == pygame.K_s:
            self.left_paddle.moving_down = True
        # right_paddle keydown events
        elif event.key == pygame.K_i:
            self.right_paddle.moving_up = True
        elif event.key == pygame.K_k:
            self.right_paddle.moving_down = True
        # System keydown events
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        # left_paddle keyup events
        if event.key == pygame.K_w:
            self.left_paddle.moving_up = False
        elif event.key == pygame.K_s:
            self.left_paddle.moving_down = False
        # left_paddle keyup events
        elif event.key == pygame.K_i:
            self.right_paddle.moving_up = False
        elif event.key == pygame.K_k:
            self.right_paddle.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.left_paddle.draw_paddle()
        self.right_paddle.draw_paddle()
        pygame.display.flip()

if __name__ == '__main__':
    pong = Pong()
    pong.run_game()
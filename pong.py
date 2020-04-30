import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from paddle import Paddle
from ball import Ball

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

        self.stats = GameStats(self)

        self.play_button = Button(self, "Play")
        self.screen_rect = self.screen.get_rect()

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self._check_ball_location()
                self._check_paddle_ball_collision()
                self.left_paddle.update()
                self.right_paddle.update()
                self.ball.update()
            self._update_screen()

    def _create_game_elements(self):
        self.left_paddle = Paddle(self, 'left')
        self.right_paddle = Paddle(self, 'right')

        self.ball = Ball(self)

        # Store all game sprites in a managable group.
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.left_paddle)
        self.sprites.add(self.right_paddle)
        self.sprites.add(self.ball)
        
    def _check_events(self):
        """"Listen for when user presses buttons"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self._create_game_elements()
            pygame.mouse.set_visible(False)


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
        # right_paddle keyup events
        elif event.key == pygame.K_i:
            self.right_paddle.moving_up = False
        elif event.key == pygame.K_k:
            self.right_paddle.moving_down = False

    def _check_ball_location(self):
        # Bounces on the top or bottom of the surface
        # Scores a goal on the left or right end of the surface
        if self.ball.rect.y >= self.screen_rect.bottom:
            self.ball.y_velocity *= -1
        if self.ball.rect.y <= self.screen_rect.top:
            self.ball.y_velocity *= -1
        if self.ball.rect.x < self.screen_rect.left or self.ball.rect.x >= self.screen_rect.right:
            self._goal()

    def _check_paddle_ball_collision(self):
        if pygame.sprite.collide_rect(self.ball, self.left_paddle) or pygame.sprite.collide_rect(self.ball, self.right_paddle):
            self.ball.x_velocity *= -1
            self.stats.rally_length += 1
            if self.stats.rally_length > 0:
                if self.stats.rally_length % 3 == 0:
                    self.settings.increase_speed()
            print(self.stats.rally_length)

    def _goal(self):
        """Respond to the ball getting past a paddle"""
        self.sprites.empty()
        self.stats.game_active = False
        pygame.mouse.set_visible(True)
        # self._reset_game()
        # sleep(2)
        # if statement for scores under 10. if score over ten game active false

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        if self.stats.game_active:
            self.left_paddle.draw()
            self.right_paddle.draw()
            self.ball.draw()
            print(self.ball.rect)
        # Draw play button if game is inactive
        elif not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

if __name__ == '__main__':
    pong = Pong()
    pong.run_game()
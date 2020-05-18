import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from random import randint
from bullet import Bullet
from sound import Sound

class Pong:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
    
        pygame.display.set_caption("Pong")
        self.sound = Sound()
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self._check_ball_location()
                self._check_paddle_ball_collision()
                self._check_bullet_ball_collision()
                self.left_paddle.update()
                self.right_paddle.update()
                self.ball.update()
                self._update_bullets()
            self._update_screen()

    def _create_game_elements(self):
        self.settings.initialize_dynamic_settings()
        self.left_paddle = Paddle(self, 'left')
        self.right_paddle = Paddle(self, 'right')
        self.ball = Ball(self)

        self.left_paddle_bullets = pygame.sprite.Group()
        self.right_paddle_bullets = pygame.sprite.Group()

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
            self.sb.prep_score()
            self.stats.game_active = True
            self._create_game_elements()
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        # left_paddle keydown events
        if event.key == pygame.K_e:
            self.left_paddle.moving_up = True
        elif event.key == pygame.K_d:
            self.left_paddle.moving_down = True
        elif event.key == pygame.K_c:
            self._fire_bullet(self.left_paddle)
        # right_paddle keydown events
        elif event.key == pygame.K_y:
            self.right_paddle.moving_up = True
        elif event.key == pygame.K_h:
            self.right_paddle.moving_down = True
        elif event.key == pygame.K_n:
            self._fire_bullet(self.right_paddle)
        # System keydown events
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        # left_paddle keyup events
        if event.key == pygame.K_e:
            self.left_paddle.moving_up = False
        elif event.key == pygame.K_d:
            self.left_paddle.moving_down = False
        # right_paddle keyup events
        elif event.key == pygame.K_y:
            self.right_paddle.moving_up = False
        elif event.key == pygame.K_h:
            self.right_paddle.moving_down = False

    def _check_ball_location(self):
        # Bounces on the top or bottom of the surface
        if self.ball.rect.bottom >= self.screen_rect.bottom:
            self._bounce(1)
        if self.ball.rect.top <= self.screen_rect.top:
            self._bounce(1)
        # Scores a goal on the left or right end of the surface
        if self.ball.rect.x < self.screen_rect.left:
            self._goal(self.right_paddle)
        if self.ball.rect.x >= self.screen_rect.right:
            self._goal(self.left_paddle)

    def _check_paddle_ball_collision(self):
        if (pygame.sprite.collide_rect(self.ball, self.left_paddle) or 
            pygame.sprite.collide_rect(self.ball, self.right_paddle)):
            if self._check_rim_shot():
                self._bounce(1)
            else:
                self._normal_shot()  

    def _normal_shot(self):
        self._bounce(0)
        self._chaos_generator()
        self.stats.rally_length += 1
        if self.stats.rally_length > 0:
            if self.stats.rally_length % 3 == 0:
                self.settings.increase_speed()

    def _check_rim_shot(self):
        if (self.ball.rect.left < (self.left_paddle.rect.right - 20) or 
            self.ball.rect.right > (self.right_paddle.rect.left + 20)):
            return True

    def _bounce(self, axis):
        self.settings.velocity[axis] *= -1

    def _check_bullet_ball_collision(self):
        """ Bullets make the ball change y velocity. X velocity is modified so
        that the ball is moving away from the paddle """
        left_collided = pygame.sprite.spritecollideany(self.ball, self.left_paddle_bullets)
        if left_collided:
            self._ricochet()
            self.left_paddle_bullets.remove(left_collided)
            if self.settings.velocity[0] < 0:
                self._reflect_bullet()

        right_collided = pygame.sprite.spritecollideany(self.ball, self.right_paddle_bullets)
        if right_collided:
            self._ricochet()
            self.right_paddle_bullets.remove(right_collided)
            if self.settings.velocity[0] > 0:
                self._reflect_bullet()

    def _ricochet(self):
        if abs(self.settings.velocity[1]) > abs(self.settings.velocity[0]):
            self.settings.velocity[0] = self.settings.velocity[0] / (self.settings.velocity[0] / self.settings.velocity[1])
            self.settings.velocity[1] = (self.settings.velocity[1] * (self.settings.velocity[0] / self.settings.velocity[1])) * ((-1) ** randint(2,3))
        else:
            self.settings.velocity[1] *= -1
        self._chaos_generator()
        self.sound.ricochet()

    def _reflect_bullet(self):
        self._bounce(0)

    def _chaos_generator(self):
        """ Adjust velocity of ball slightly after paddle/ball collision
        to make game more interesting
        """
        chaos_index = (randint(-10, 25) / 100) + 1
        # Chaos index will be more likely to make y velocity more accute,
        # otherwise points can go on too long.
        self.settings.velocity[1] *= chaos_index

    def _goal(self, paddle):
        """Respond to the ball getting past a paddle"""
        if self.left_paddle == paddle:
            self.stats.score[0] += 1
        elif self.right_paddle == paddle:
            self.stats.score[1] += 1

        self.sb.prep_score()
        self._update_screen()
        sleep(1)
        self._check_score()
        self.sprites.empty()

    def _fire_bullet(self, paddle):
        """Create a new bullet and add it to the bullets group"""
        if self.left_paddle == paddle:
            if len(self.left_paddle_bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self, self.left_paddle)
                self.left_paddle_bullets.add(new_bullet)
                self.sound.fire()

        if self.right_paddle == paddle:
            if len(self.right_paddle_bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self, self.right_paddle)
                self.right_paddle_bullets.add(new_bullet)
                self.sound.fire()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.left_paddle_bullets.update()
        self.right_paddle_bullets.update()

        # Delete old bullets when they leave the screen
        # Loop through copy of list because not possible to change list 
        # length during a loop
        for bullet in self.left_paddle_bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.left_paddle_bullets.remove(bullet)

        for bullet in self.right_paddle_bullets.copy():
            if bullet.rect.right <= self.screen_rect.left:
                self.right_paddle_bullets.remove(bullet)

    def _check_score(self):
        if self.stats.score[0] >= self.settings.play_to or self.stats.score[1] >= self.settings.play_to:
            sleep(3)
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

        self._reset_game()

    def _reset_game(self):
        self._create_game_elements()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        if self.stats.game_active:
            self.sb.show_score()
            self.left_paddle.draw()
            self.right_paddle.draw()
            self.ball.draw()
            for bullet in self.left_paddle_bullets.sprites():
                bullet.draw_bullet()
            for bullet in self.right_paddle_bullets.sprites():
                bullet.draw_bullet()
        # Draw play button if game is inactive
        elif not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

if __name__ == '__main__':
    pong = Pong()
    pong.run_game()

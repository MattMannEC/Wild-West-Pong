import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):

    def __init__(self, pong_game):
        super().__init__()
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = pong_game.settings

        self.rect = pygame.Rect(self.screen_rect.centerx, 
            self.screen_rect.centery, 
            (self.settings.ball_width * pong_game.relative_unit), 
            (self.settings.ball_height * pong_game.relative_unit))
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # X axis is randomly + or - a relative_unit
        self.serve_x = pong_game.relative_unit * ((-1) ** randint(2,3))
        # Y axis is random number between 1 and 2 either positive or 
        # negative multiplied by one relative_unit
        self.serve_y = ((pong_game.relative_unit * randint(10, 12)/10) * 
            (-1) ** randint(2,3))

        self.settings.velocity = [self.serve_x, self.serve_y]

    def update(self, pong_game):
        # Update x axis position
        self.x += (self.settings.velocity[0] * pong_game.relative_unit)
        self.rect.x = self.x

        # Update y axis position
        self.y += self.limit_y_velocity(pong_game)
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.ball_color, self.rect)

    def limit_y_velocity(self, pong_game):
        if self.settings.velocity[1] > (pong_game.relative_unit *
            self.settings.max_y):
            print("max")
            return self.settings.max_y
        elif self.settings.velocity[1] < (pong_game.relative_unit * 
            self.settings.min_y):
            print("min")
            return self.settings.min_y
        else:
            return self.settings.velocity[1]




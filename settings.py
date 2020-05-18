class Settings:
    def __init__(self):
    
        # Screen settings
        self.screen_width = 0
        self.screen_height = 0
        self.bg_color = (0, 0, 0)

        # Player 1 controls
        self.p1_up = "w"
        self.p1_down = "s"
        self.p1_fire = "x"

        # Player 2 controls
        self.p2_up = "y"
        self.p2_down = "h"
        self.p2_fire = "n"

        # Paddle settings
        self.paddle_width = 20
        self.paddle_height = 300
        self.paddle_color = (255, 255, 255)

        # Balls settings
        self.ball_width = 50
        self.ball_height = 50
        self.ball_color = (255, 255, 255)
        self.max_y = 40
        self.min_y = -40

        # Bullet settings
        self.bullet_width = 25
        self.bullet_height = 5
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 2

        # Game settings
        self.play_to = 3
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.paddle_speed = 6
        self.velocity = []
        self.bullet_speed = 8

    def increase_speed(self):
        """Speed the game up gradually during each point.
        The longer a point goes on the faster it gets.
        """
        self.paddle_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.velocity[0] *= self.speedup_scale
        self.velocity[1] *= self.speedup_scale
        ### write loop for value in velocity to be multiplied by speedup scale
        

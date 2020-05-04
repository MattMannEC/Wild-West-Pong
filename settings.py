class Settings:
    def __init__(self):
    
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Paddle settings
        self.paddle_width = 2
        self.paddle_height = 200
        self.paddle_color = (255, 255, 255)

        # Balls settings
        self.ball_width = 50
        self.ball_height = 50
        self.ball_color = (255, 255, 255)
        self.max_y = 8
        self.min_y = -8

        # Bullet settings
        self.bullet_speed = 2
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
        self.paddle_speed = 1.5
        self.velocity = []

    def increase_speed(self):
        """Speed the game up gradually during each point.
        The longer a point goes on the faster it gets.
        """
        self.paddle_speed *= self.speedup_scale
        self.velocity[0] *= self.speedup_scale
        self.velocity[1] *= self.speedup_scale
        ### write loop for value in velocity to be multiplied by speedup scale
        
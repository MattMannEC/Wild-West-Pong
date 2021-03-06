class Settings:
    def __init__(self):
    
        # Screen settings
        self.bg_color = (0, 0, 0)

        # Paddle settings
        self.paddle_width = 10
        self.paddle_height = 200
        self.paddle_color = (255, 255, 255)

        # Balls settings
        self.ball_width = 40
        self.ball_height = 40
        self.ball_color = (255, 255, 255)
        self.max_y = 40
        self.min_y = -40

        # Bullet settings
        self.bullet_width = 30
        self.bullet_height = 4
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 2

        # Game settings
        self.play_to = 3
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.paddle_speed = 3
        self.velocity = []
        self.bullet_speed = 5

    def increase_speed(self):
        """Speed the game up gradually during each point.
        The longer a point goes on the faster it gets.
        """
        self.paddle_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.velocity[0] *= self.speedup_scale
        self.velocity[1] *= self.speedup_scale
        ### write loop for value in velocity to be multiplied by speedup scale
        

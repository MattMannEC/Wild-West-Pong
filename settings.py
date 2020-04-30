class Settings:
    def __init__(self):
    
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Paddle settings
        self.paddle_width = 50
        self.paddle_height = 200
        self.paddle_color = (255, 0, 144)

        # Balls settings
        self.ball_width = 10
        self.ball_height = 10
        self.ball_color = (0, 0, 0)
        
        # How quickly the game speeds up
        self.speedup_scale = 2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.paddle_speed = 1.5
        #### Create velocity list setting
        self.ball_speed = 3

    def increase_speed(self):
        """Speed the game up gradually during each point.
        The longer a point goes on the faster it gets.
        """
        self.paddle_speed *= self.speedup_scale

        ### write loop for value in velocity to be multiplied by speedup scale
        self.ball_speed *= self.speedup_scale
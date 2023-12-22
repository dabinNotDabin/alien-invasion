from alien import Alien


class Settings:
    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 800
        self.background_colour = (230, 230, 230)
        self.num_bullets_allowed = 3
        self.alien_width = Alien((0, 0)).rect.width
        self.alien_height = Alien((0, 0)).rect.height

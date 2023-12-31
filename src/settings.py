class Settings:
    STARTING_SHIPS: int = 3

    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 800
        self.background_colour = (230, 230, 230)
        self.max_bullets = 3
        self.ship_hit_sleep_time_seconds = 1.0
        self.speedup_factor = 1.2

import sys

import pygame

from event_handler import EventHandler
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Alien fkin Invasion")

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.screen.fill(self.settings.background_colour)

        self.clock = pygame.time.Clock()

        self.event_handler = EventHandler()

        shipSpeed = 3.0
        self.ship = Ship(shipSpeed, self.screen.get_rect().midbottom)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            self.event_handler.handle(event)

        if self.event_handler.is_moving_left:
            self.ship.move_left()
        if self.event_handler.is_moving_right:
            self.ship.move_right()

    def _update_screen(self):
        self.ship.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()

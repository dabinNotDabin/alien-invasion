import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self) -> None:
        self.settings = Settings()
        pygame.init()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Alien fkin Invasion")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.background_colour)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()

import sys

import pygame

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
        self.ship = Ship(self.screen.get_rect().midbottom)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                self._handle_key_down(event)

    def _handle_key_down(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move(2, 0)
        if event.key == pygame.K_LEFT:
            self.ship.move(-2, 0)

    def _update_screen(self):
        self.ship.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()

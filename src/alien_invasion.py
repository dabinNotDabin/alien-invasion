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
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.clock = pygame.time.Clock()

        self.event_handler = EventHandler()

        shipSpeed = 5.0
        self.ship = Ship(shipSpeed, self.screen.get_rect().midbottom)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            self._check_for_quit(event)
            self.event_handler.handle(event)

        if self.event_handler.is_moving_left:
            self.ship.move_left(self.screen)
        if self.event_handler.is_moving_right:
            self.ship.move_right(self.screen)

    def _check_for_quit(self, event):
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_q
        ):
            sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.background_colour)
        self.ship.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()

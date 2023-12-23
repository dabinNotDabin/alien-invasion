import sys

import pygame

from aliens import Aliens
from bullets import Bullets
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Alien fkin Invasion")

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.clock = pygame.time.Clock()

        self.is_moving_left = False
        self.is_moving_right = False

        screen_rect = self.screen.get_rect()
        self.ship = Ship(screen_rect)

        self.bullets = Bullets(self.settings.max_bullets)
        self.aliens = Aliens(screen_rect)

    def run_game(self):
        while True:
            self._process_events()
            self.ship.update()
            self.bullets.update()
            self.aliens.update()
            self._update_screen()
            self.clock.tick(60)

    def _process_events(self):
        for event in pygame.event.get():
            self._process_key_presses(event)

    def _process_key_presses(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            sys.exit()

        if event.type == pygame.KEYDOWN:
            self._handle_key_down(event)

        if event.type == pygame.KEYUP:
            self._handle_key_up(event)

    def _handle_key_down(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.set_moving_left()
        elif event.key == pygame.K_RIGHT:
            self.ship.set_moving_right()
        elif event.key == pygame.K_SPACE:
            self.bullets.fire_bullet(self.ship.rect.midtop)

    def _handle_key_up(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.stop_moving_left()
        elif event.key == pygame.K_RIGHT:
            self.ship.stop_moving_right()

    def _update_screen(self):
        self.screen.fill(self.settings.background_colour)
        self.ship.draw(self.screen)
        self.bullets.draw(self.screen)
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()

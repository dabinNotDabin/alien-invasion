import sys

import pygame

from alien_settings import AlienSettings
from aliens import Aliens
from bullets import Bullets
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Alien fkin Invasion")

        self.settings = Settings()
        self.alien_settings = AlienSettings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.clock = pygame.time.Clock()

        self.is_moving_left = False
        self.is_moving_right = False

        ship_speed = 5.0
        self.ship = Ship(ship_speed, self.screen.get_rect().midbottom)

        self.bullets = Bullets(self.settings.max_bullets)
        self.aliens = Aliens(self.screen.get_rect().topleft, self.screen.get_rect().bottomright)

    def run_game(self):
        while True:
            self._check_events()
            self.bullets.update()
            self.aliens.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            self._check_for_quit(event)
            self._check_key_presses(event)

        if self.is_moving_left:
            self.ship.move_left(self.screen)
        if self.is_moving_right:
            self.ship.move_right(self.screen)

    def _check_for_quit(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            sys.exit()

    def _check_key_presses(self, event):
        if event.type == pygame.KEYDOWN:
            self._handle_key_down(event)

        if event.type == pygame.KEYUP:
            self._handle_key_up(event)

    def _handle_key_down(self, event):
        if event.key == pygame.K_LEFT:
            self.is_moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.is_moving_right = True
        elif event.key == pygame.K_SPACE:
            self.bullets.fire_bullet(self.ship.rect.midtop)

    def _handle_key_up(self, event):
        if event.key == pygame.K_LEFT:
            self.is_moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.is_moving_right = False

    def _update_screen(self):
        self.screen.fill(self.settings.background_colour)
        self.ship.draw(self.screen)
        self.bullets.draw(self.screen)
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()

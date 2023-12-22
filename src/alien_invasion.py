import sys

import pygame

from alien import Alien
from bullet import Bullet
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Alien fkin Invasion")

        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200, 800))

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.clock = pygame.time.Clock()

        self.is_moving_left = False
        self.is_moving_right = False

        ship_speed = 5.0
        self.ship = Ship(ship_speed, self.screen.get_rect().midbottom)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.bullets.update()
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
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_q
        ):
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
            self._fire_bullet()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.num_bullets_allowed:
            bullet = Bullet(self.ship.rect.midtop)
            self.bullets.add(bullet)

    def _handle_key_up(self, event):
        if event.key == pygame.K_LEFT:
            self.is_moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.is_moving_right = False

    def _create_fleet(self):
        alien = Alien()
        self.aliens.add(alien)

    def _update_screen(self):
        self.screen.fill(self.settings.background_colour)
        self.ship.draw(self.screen)
        self._draw_bullets()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _draw_bullets(self):
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            else:
                bullet.draw(self.screen)


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()

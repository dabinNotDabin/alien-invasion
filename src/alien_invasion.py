import sys
from time import sleep

import pygame

from alien_fleet import AlienFleet
from bullets import Bullets
from button import TextButton
from settings import Settings
from ship import Ship
from stats import EventType, Stats


class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Alien fkin Invasion")

        self.settings = Settings()
        self.stats = Stats()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.clock = pygame.time.Clock()

        screen_rect = self.screen.get_rect()
        self.ship = Ship(screen_rect)

        self.bullets = Bullets(self.settings.max_bullets)
        self.aliens = AlienFleet(screen_rect)

        self.is_active = False
        self.play_button = TextButton(screen_rect, "Play")

    def run_game(self):
        while True:
            self._process_events()

            if self.is_active:
                self._process_collisions()
                self.ship.update()
                self.bullets.update()
                self.aliens.update()
                self._check_for_empty_fleet()

            self._update_screen()
            self.clock.tick(60)

    def _process_events(self):
        for event in pygame.event.get():
            self._process_event(event)

    def _process_event(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            sys.exit()

        if event.type == pygame.KEYDOWN:
            self._handle_key_down(event)

        if event.type == pygame.KEYUP:
            self._handle_key_up(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            self._handle_mouse_down()

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

    def _handle_mouse_down(self):
        mouse_pos = pygame.mouse.get_pos()
        if not self.is_active and self.play_button.rect.collidepoint(mouse_pos):
            self.is_active = True
            self._reset_game()
            self.stats = Stats()
            pygame.mouse.set_visible(False)

    def _process_collisions(self):
        pygame.sprite.groupcollide(self.bullets.bullets, self.aliens.aliens, True, True)

        is_ship_alien_collision = pygame.sprite.spritecollideany(self.ship, self.aliens.aliens)
        if is_ship_alien_collision or self.aliens.is_alien_at_bottom():
            self.stats.record(EventType.SHIP_HIT)
            if self.stats.ships_left > 0:
                sleep(self.settings.ship_hit_sleep_time_seconds)
                self._reset_game()
            else:
                self._game_over()

    def _reset_game(self):
        self.aliens.empty()
        self.bullets.empty()
        self.aliens.create_fleet()
        self.ship.reposition(self.screen.get_rect().midbottom)

    def _game_over(self):
        self.is_active = False
        self.aliens = AlienFleet(self.screen.get_rect())
        self.bullets = Bullets(self.settings.max_bullets)
        self.ship = Ship(self.screen.get_rect())

    def _check_for_empty_fleet(self):
        if not self.aliens.aliens:
            self.bullets.empty()
            self.aliens.create_fleet()

            self.ship.increase_speed(self.settings.speedup_factor)
            self.aliens.increase_speed(self.settings.speedup_factor)
            self.bullets.increase_speed(self.settings.speedup_factor)

    def _update_screen(self):
        self.screen.fill(self.settings.background_colour)
        self.ship.draw(self.screen)
        self.bullets.draw(self.screen)
        self.aliens.draw(self.screen)

        if not self.is_active:
            self.play_button.draw(self.screen)
            pygame.mouse.set_visible(True)

        pygame.display.flip()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()

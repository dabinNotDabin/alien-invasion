from typing import Any, override

import pygame
from pygame.surface import Surface

from alien import Alien
from alien_settings import AlienSettings
from direction import Direction


class AlienFleet(pygame.sprite.Group):
    def __init__(self, screen_rect: pygame.Rect) -> None:
        self.alien_settings = AlienSettings()
        self.aliens = pygame.sprite.Group()
        self.screen_rect = screen_rect

        self.create_fleet()

    def create_fleet(self):
        self.alien_settings.direction = Direction.RIGHT

        screen_rect = self.screen_rect
        max_x = screen_rect.right - self.alien_settings.width
        max_y = screen_rect.bottom - 3 * self.alien_settings.height
        alien_spacing = 2 * self.alien_settings.width

        current_pos = screen_rect.topleft
        while current_pos[0] < max_y:
            while current_pos[1] < max_x:
                self.aliens.add(Alien(current_pos, screen_rect, self.alien_settings))
                current_pos = (current_pos[0], current_pos[1] + alien_spacing)

            current_pos = (current_pos[0] + alien_spacing, screen_rect.left)

    @override
    def empty(self) -> None:
        return self.aliens.empty()

    @override
    def update(self, *args: Any, **kwargs: Any) -> None:
        self.aliens.update()

        alien: Alien
        for alien in self.aliens.sprites():
            if alien.hit_edge():
                self._advance_fleet()
                break

    def _advance_fleet(self):
        alien: Alien
        for alien in self.aliens.sprites():
            alien.move_down()

        self.alien_settings.direction = Direction.opposite(self.alien_settings.direction)

    def draw(self, screen: Surface) -> None:
        self.aliens.draw(screen)

    def is_alien_at_bottom(self) -> bool:
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                return True

        return False

    def increase_speed(self, factor: float):
        self.alien_settings.speed *= factor

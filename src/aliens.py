from typing import Any, override

import pygame
from pygame.surface import Surface

from alien import Alien
from alien_settings import AlienSettings


class Aliens(pygame.sprite.Group):
    def __init__(self, screen_rect: pygame.Rect) -> None:
        self.settings = AlienSettings()
        self.aliens = pygame.sprite.Group()

        self._create_fleet(screen_rect)

    @override
    def update(self, *args: Any, **kwargs: Any) -> None:
        self.aliens.update()

    def draw(self, screen: Surface) -> None:
        self.aliens.draw(screen)

    def _create_fleet(self, screen_rect: pygame.Rect):
        max_x = screen_rect.right - self.settings.width
        max_y = screen_rect.bottom - 3 * self.settings.height
        alien_spacing = 2 * self.settings.width

        current_pos = screen_rect.topleft
        while current_pos[0] < max_y:
            while current_pos[1] < max_x:
                self.aliens.add(Alien(current_pos))
                current_pos = (current_pos[0], current_pos[1] + alien_spacing)

            current_pos = (current_pos[0] + alien_spacing, screen_rect.left)

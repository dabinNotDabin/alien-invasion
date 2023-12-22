from typing import Any, Tuple, override

import pygame
from pygame.surface import Surface

from alien import Alien
from alien_settings import AlienSettings


class Aliens(pygame.sprite.Group):
    def __init__(self, top_left: Tuple[float, float], bottom_right: Tuple[float, float]) -> None:
        self.settings = AlienSettings()
        self.aliens = pygame.sprite.Group()

        self._create_fleet(top_left, bottom_right)

    @override
    def update(self, *args: Any, **kwargs: Any) -> None:
        self.aliens.update()

    def draw(self, screen: Surface) -> None:
        self.aliens.draw(screen)

    def _create_fleet(self, top_left: Tuple[float, float], bottom_right: Tuple[float, float]):
        max_x = bottom_right[0] - self.settings.width
        max_y = bottom_right[1] - 3 * self.settings.height
        alien_spacing = 2 * self.settings.width

        current_pos = top_left
        while current_pos[0] < max_y:
            while current_pos[1] < max_x:
                self.aliens.add(Alien(current_pos))
                current_pos = (current_pos[0], current_pos[1] + alien_spacing)

            current_pos = (current_pos[0] + alien_spacing, top_left[1])

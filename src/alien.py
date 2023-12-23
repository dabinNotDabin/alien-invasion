from typing import Any, Tuple, override

import pygame
from pygame.sprite import Sprite

from alien_settings import AlienSettings


class Alien(Sprite):
    def __init__(self, top_left: Tuple[int, int]) -> None:
        super().__init__()

        self.settings = AlienSettings()

        self.image = pygame.image.load("./images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.y = top_left[0]
        self.rect.x = top_left[1]

        self.x = float(self.rect.x)

    @override
    def update(self, *args: Any, **kwargs: Any) -> None:
        self.x += self.settings.speed * self.settings.direction
        self.rect.x = self.x

from typing import TYPE_CHECKING, Any, Tuple, override

import pygame
from pygame.sprite import Sprite

from alien_settings import AlienSettings

if TYPE_CHECKING:
    from pygame import Surface


class Alien(Sprite):
    def __init__(self, startingTopLeft: Tuple[int, int]) -> None:
        super().__init__()

        self.settings = AlienSettings()

        self.image = pygame.image.load("./images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.y = startingTopLeft[0]
        self.rect.x = startingTopLeft[1]

        self.x = float(self.rect.x)

    @override
    def update(self, *args: Any, **kwargs: Any) -> None:
        self.x += self.settings.speed
        self.rect.x = self.x

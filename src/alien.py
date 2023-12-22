from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from pygame import Surface


class Alien(Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.image.load("./images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

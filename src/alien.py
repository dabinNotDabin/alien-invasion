from typing import TYPE_CHECKING, Tuple

import pygame
from pygame.sprite import Sprite, _Group

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

    def move_left(self, screen: "Surface"):
        if self.rect.left - self.speed >= screen.get_rect().left:
            self._move(-self.speed)

    def move_right(self, screen: "Surface"):
        if self.rect.right + self.speed <= screen.get_rect().right:
            self._move(self.speed)

    def _move(self, horizontalDistance):
        self.x += horizontalDistance
        self.rect.x = self.x

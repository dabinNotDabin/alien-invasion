from typing import TYPE_CHECKING, Tuple

import pygame

from ship_settings import ShipSettings

if TYPE_CHECKING:
    from pygame import Surface


class Ship:
    def __init__(self, startingPos: Tuple[int, int]) -> None:
        self.image = pygame.image.load("./images/ship.bmp")
        self.settings = ShipSettings()
        self.rect = self.image.get_rect()
        self.rect.midbottom = startingPos

        self.x = self.rect.x

    def draw(self, screen: "Surface"):
        screen.blit(self.image, self.rect)

    def move_left(self, screen: "Surface"):
        if self.rect.left - self.settings.speed >= screen.get_rect().left:
            self._move(-self.settings.speed)

    def move_right(self, screen: "Surface"):
        if self.rect.right + self.settings.speed <= screen.get_rect().right:
            self._move(self.settings.speed)

    def _move(self, horizontalDistance):
        self.x += horizontalDistance
        self.rect.x = self.x

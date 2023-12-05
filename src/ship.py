from typing import TYPE_CHECKING, Tuple

import pygame

if TYPE_CHECKING:
    from pygame import Surface


class Ship:
    def __init__(self, speed: float, startingPos: Tuple[int, int]) -> None:
        self.image = pygame.image.load("./images/ship.bmp")
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.midbottom = startingPos

        self.x = self.rect.x

    def draw(self, screen: "Surface"):
        screen.blit(self.image, self.rect)

    def move_left(self, screen: "Surface"):
        if self.rect.left - self.speed >= screen.get_rect().left:
            self._move(-self.speed)

    def move_right(self, screen: "Surface"):
        if self.rect.right + self.speed <= screen.get_rect().right:
            self._move(self.speed)

    def _move(self, horizontalDistance):
        self.x += horizontalDistance
        self.rect.x = self.x

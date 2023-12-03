from typing import TYPE_CHECKING, Tuple

import pygame

if TYPE_CHECKING:
    from pygame import Surface


class Ship:
    def __init__(self, startingPos: Tuple[int, int]) -> None:
        self.image = pygame.image.load("./images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = startingPos

    def draw(self, screen: "Surface"):
        screen.blit(self.image, self.rect)

    def move(self, horiztonal, vertical):
        self.rect.x += horiztonal
        self.rect.y += vertical

from ast import stmt
from typing import TYPE_CHECKING, Any, Tuple

import pygame
from pygame.sprite import Sprite

from bullet_settings import BulletSettings

if TYPE_CHECKING:
    from pygame import Surface


class Bullet(Sprite):
    def __init__(self, startingMidTop: Tuple[float, float]) -> None:
        super().__init__()

        self.settings = BulletSettings()

        self.rect = pygame.Rect(
            0,
            0,
            self.settings.width,
            self.settings.height,
        )

        self.rect.midtop = startingMidTop

        self.y = startingMidTop[1]

    def update(self):
        self.y -= self.settings.speed
        self.rect.y = self.y

    def draw(self, screen: "Surface"):
        pygame.draw.rect(screen, self.settings.colour, self.rect)

    def move_up(self, screen: "Surface"):
        self.rect.y -= self.settings.speed

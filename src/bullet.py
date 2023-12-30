from typing import TYPE_CHECKING, Any, Tuple, override

import pygame
from pygame.sprite import Sprite

from bullet_settings import BulletSettings

if TYPE_CHECKING:
    from pygame import Surface


class Bullet(Sprite):
    def __init__(self, mid_top_position: Tuple[float, float], settings: BulletSettings) -> None:
        super().__init__()

        self.settings = settings

        self.rect = pygame.Rect(
            0,
            0,
            self.settings.width,
            self.settings.height,
        )

        self.rect.midtop = mid_top_position

        self.y = mid_top_position[1]

    @override
    def update(self, *args: Any, **kwargs: Any) -> None:
        self.y -= self.settings.speed
        self.rect.y = self.y

    def draw(self, screen: "Surface"):
        pygame.draw.rect(screen, self.settings.colour, self.rect)

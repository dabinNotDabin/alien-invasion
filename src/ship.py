from typing import TYPE_CHECKING, Any, Tuple, override

import pygame
from pygame.sprite import Sprite

from ship_settings import ShipSettings

if TYPE_CHECKING:
    from pygame import Surface


class Ship(Sprite):
    def __init__(self, screen_rect: pygame.Rect) -> None:
        super().__init__()

        self.image = pygame.image.load("./images/ship.bmp")
        self.settings = ShipSettings()
        self.rect = self.image.get_rect()
        self.rect.midbottom = screen_rect.midbottom
        self.min_x = screen_rect.left
        self.max_x = screen_rect.right

        self.x = self.rect.x

    def draw(self, screen: "Surface"):
        screen.blit(self.image, self.rect)

    @override
    def update(self, *args: Any, **kwargs: Any) -> None:
        if self.settings.moving_left:
            self.move_left()
        if self.settings.moving_right:
            self.move_right()

    def move_left(self):
        if self.rect.left - self.settings.speed >= self.min_x:
            self._move(-self.settings.speed)

    def move_right(self):
        if self.rect.right + self.settings.speed <= self.max_x:
            self._move(self.settings.speed)

    def _move(self, horizontal_distance):
        self.x += horizontal_distance
        self.rect.x = self.x

    def set_moving_left(self):
        self.settings.moving_left = True

    def set_moving_right(self):
        self.settings.moving_right = True

    def stop_moving_left(self):
        self.settings.moving_left = False

    def stop_moving_right(self):
        self.settings.moving_right = False

    def reposition(self, midbottom: Tuple[float, float]):
        self.rect.midbottom = midbottom
        self.x = float(self.rect.x)

    def increase_speed(self, factor: float):
        self.settings.speed *= factor

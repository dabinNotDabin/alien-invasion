from typing import Any, Tuple, override

import pygame
from pygame.surface import Surface

from bullet import Bullet
from bullet_settings import BulletSettings


class Bullets(pygame.sprite.Group):
    def __init__(self, max_bullets: int) -> None:
        self.bullet_settings = BulletSettings()
        self.bullets = pygame.sprite.Group()
        self.max_bullets = max_bullets

    @override
    def update(self, *args: Any, **kwargs: Any) -> None:
        self.bullets.update()

    @override
    def empty(self) -> None:
        return self.bullets.empty()

    def draw(self, screen: Surface) -> None:
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            else:
                bullet.draw(screen)

    def fire_bullet(self, mid_top_position: Tuple[float, float]):
        if len(self.bullets) < self.max_bullets:
            bullet = Bullet(mid_top_position, self.bullet_settings)
            self.bullets.add(bullet)

    def increase_speed(self, factor: float):
        self.bullet_settings.speed *= factor

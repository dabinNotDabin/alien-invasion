import enum

import pygame


class AlienSettings:
    def __init__(self) -> None:
        self.speed = 1.0
        self.fleet_direction = FleetDirection.RIGHT

        alien_image_rect = pygame.image.load("./images/alien.bmp").get_rect()
        self.width = alien_image_rect.width
        self.height = alien_image_rect.height


class FleetDirection(enum.IntEnum):
    LEFT = -1
    RIGHT = 1

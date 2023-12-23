import pygame

from direction import Direction


class AlienSettings:
    def __init__(self) -> None:
        self.speed = 1.0
        self.vertical_speed = 10.0
        self.direction = Direction.RIGHT

        alien_image_rect = pygame.image.load("./images/alien.bmp").get_rect()
        self.width = alien_image_rect.width
        self.height = alien_image_rect.height

import pygame


class AlienSettings:
    def __init__(self) -> None:
        self.alien_speed = 1.0

        alien_image_rect = pygame.image.load("./images/alien.bmp").get_rect()

        self.width = alien_image_rect.width
        self.height = alien_image_rect.height

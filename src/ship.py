import pygame

from alien_invasion import AlienInvasion


class Ship:
    def __init__(self, game: AlienInvasion) -> None:
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("../images/ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

import pygame
from pygame import Rect, Surface


class TextButton:
    def __init__(self, screen_rect: Rect, text) -> None:
        self.width = 200
        self.height = 50
        self.button_colour = (0, 135, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = screen_rect.center

        self.rendered_text = self.font.render(text, True, self.text_colour, self.button_colour)
        self.text_rect = self.rendered_text.get_rect()
        self.text_rect.center = self.rect.center

    def draw(self, screen: Surface):
        screen.fill(self.button_colour, self.rect)
        screen.blit(self.rendered_text, self.text_rect)

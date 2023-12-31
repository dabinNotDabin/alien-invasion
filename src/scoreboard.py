import pygame
from pygame import Rect, Surface

from settings import Settings
from stats import Stats


class Scoreboard:
    def __init__(self, screen_rect: Rect) -> None:
        self.screen_rect = screen_rect

        self.text_colour = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

    def draw(self, screen: Surface, stats: Stats):
        rendered_score = self.font.render(str(stats.score), True, self.text_colour, Settings.BACKGROUND_COLOUR)
        score_rect = rendered_score.get_rect()
        score_rect.right = self.screen_rect.right - 20
        score_rect.top = 20

        screen.blit(rendered_score, score_rect)

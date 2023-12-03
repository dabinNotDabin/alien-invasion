import pygame


class EventHandler:
    def __init__(self) -> None:
        self.is_moving_left = False
        self.is_moving_right = False

    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.is_moving_left = True
            elif event.key == pygame.K_RIGHT:
                self.is_moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.is_moving_left = False
            elif event.key == pygame.K_RIGHT:
                self.is_moving_right = False

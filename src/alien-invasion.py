import sys

import pygame

from settings import Settings


class AlienInvasion:
    def __init__(self) -> None:
        self.settings = Settings()
        pygame.init()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_height, self.settings.screen_width)
        )

        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Alien fkin Invasion")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.background_colour)

            pygame.display.flip()

            self.clock.tick(60)


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()

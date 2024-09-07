import sys

import pygame

from Modules.UI.text import Text
from Modules.player import Player
from data.constants import SCREEN_WIDTH, SCREEN_HEIGHT, DISPLAY_GAME_OVER


class Elements(Text):

    def __init__(self):
        super().__init__()
        self.score_value = 0

    def draw(self, screen):
        self.score(screen)
        self.lives(screen)

    def score(self, screen):
        val = f'Score: {str(self.score_value)}'
        coordinates = (20, 20)
        text = self.font.render(val, True, 'white')
        screen.blit(text, coordinates)

    def lives(self, screen):
        val = f'Lives: {Player.lives + 1}'
        coordinates = (20, 50)
        text = self.font.render(val, True, 'white')
        screen.blit(text, coordinates)

    def game_over(self, screen):
        val = f'GAME OVER!'
        coordinates = (SCREEN_WIDTH / 2 - (130 / 2), SCREEN_HEIGHT / 2 - 20)

        screen.fill('black')

        text = self.font.render(val, True, 'white')
        screen.blit(text, coordinates)

        pygame.display.flip()
        pygame.time.wait(DISPLAY_GAME_OVER)

        raise sys.exit('Game over!')

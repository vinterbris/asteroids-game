import pygame

from Modules.UI.text import Text
from Modules.player import Player
from data.constants import SCREEN_WIDTH


class Elements(Text):

    def __init__(self):
        super().__init__()
        self.value = 0

    def draw(self, screen):
        self.score(screen)
        self.lives(screen)

    def score(self, screen):
        val = f'Score: {str(self.value)}'
        coordinates = (20, 20)
        text = self.font.render(val, True, 'white')
        screen.blit(text, coordinates)

    def lives(self, screen):
        val = f'Lives: {Player.lives + 1}'
        coordinates = (20, 50)
        text = self.font.render(val, True, 'white')
        screen.blit(text, coordinates)

import pygame


class Text(pygame.sprite.Sprite):

    def __init__(self):
        self.font_size = 21
        self.bold = True
        self.font = pygame.font.SysFont("Helvetica", self.font_size, self.bold)
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

    def draw(self, screen):
        pass

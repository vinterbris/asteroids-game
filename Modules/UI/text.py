import pygame


class Text(pygame.sprite.Sprite):

    def __init__(self):
        self.font = pygame.font.SysFont("Helvetica", 21)
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

    def draw(self, screen):
        pass

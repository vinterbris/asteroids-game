import pygame

from Modules.circleshape import CircleShape


class Particle(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, 2)
        self.lifetime = 50

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 4)

    def update(self, dt):
        self.position += self.velocity * dt

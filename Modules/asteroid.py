import pygame.draw

from circleshape import CircleShape
from data.constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)

        splitted_radius = self.radius - ASTEROID_MIN_RADIUS

        splitted_asteroid1 = Asteroid(self.position.x, self.position.y, splitted_radius)
        splitted_asteroid2 = Asteroid(self.position.x, self.position.y, splitted_radius)

        splitted_asteroid1.velocity = vector1 * 1.2
        splitted_asteroid2.velocity = vector2 * 1.2

import random

import pygame.draw

from Modules.circleshape import CircleShape
from Modules.particle import Particle
from data.constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, score):
        self.kill()
        self.explode()
        if self.radius == ASTEROID_MIN_RADIUS:
            score.score_value += 80
            return

        if self.radius == ASTEROID_MAX_RADIUS:
            score.score_value += 20
        else:
            score.score_value += 50

        angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)

        splitted_radius = self.radius - ASTEROID_MIN_RADIUS

        splitted_asteroid1 = Asteroid(self.position.x, self.position.y, splitted_radius)
        splitted_asteroid2 = Asteroid(self.position.x, self.position.y, splitted_radius)

        splitted_asteroid1.velocity = vector1 * 1.2
        splitted_asteroid2.velocity = vector2 * 1.2

    def explode(self):
        particles = []
        amount = random.randint(3, 6)
        for _ in range(amount):
            angle = random.uniform(0, 360)
            vector = self.velocity.rotate(angle)
            particle = Particle(self.position.x, self.position.y)
            particle.velocity = vector * 1.5
            particles.append(particle)

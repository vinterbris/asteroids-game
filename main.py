import pygame

from Modules.UI.elements import Elements
from Modules.asteroid import Asteroid
from Modules.asteroidfield import AsteroidField
from Modules.particle import Particle
from Modules.player import Player
from Modules.shot import Shot
from data.constants import *


def main():
    # Initialization
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    particles = pygame.sprite.Group()
    ui = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    Elements.containers = (ui, drawable)
    Particle.containers = (particles, drawable, updatable)

    # Objects
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ui_elements = Elements()
    particle = Particle(0, 0)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')

        # update
        for obj in updatable:
            obj.update(dt)

        # check collisions
        for asteroid in asteroids:
            if asteroid.collide_with(player):
                if Player.lives > 0:
                    player = player.respawn()
                else:
                    ui_elements.game_over(screen)
            for shot in shots:
                if asteroid.collide_with(shot):
                    asteroid.split(ui_elements)
                    shot.kill()

        for particle in particles:
            if particle.lifetime > 0:
                particle.lifetime -= 1
            else:
                particle.kill()

        # draw
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

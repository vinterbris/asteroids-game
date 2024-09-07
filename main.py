import sys

import pygame

from Modules.asteroid import Asteroid
from Modules.asteroidfield import AsteroidField
from Modules.UI.elements import Elements
from data.constants import *
from Modules.player import Player
from Modules.shot import Shot


def main():
    # Initialization
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    font = pygame.font.SysFont("Arial", 20)

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    ui = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    Elements.containers = (ui, drawable)

    # Objects
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    score = Elements()

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
                    player.kill()
                    Player.lives -= 1
                    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                else:
                    raise sys.exit('Game over!')
            for shot in shots:
                if asteroid.collide_with(shot):
                    asteroid.split(score)
                    shot.kill()

        # draw
        for obj in drawable:
            obj.draw(screen)

        # score_text = font.render(f"Score: {score.value}", True, 'white')
        # screen.blit(score_text, (20, 20))

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

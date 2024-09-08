import pygame

from Modules.circleshape import CircleShape
from Modules.shot import Shot
from data.constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLAYER_MAX_SPEED,
    PLAYER_ACCELERATION,
    PLAYER_DECELERATION,
)


class Player(CircleShape):
    lives = 2

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.max_speed = PLAYER_MAX_SPEED
        self.speed = PLAYER_SPEED
        self.acceleration = PLAYER_ACCELERATION
        self.deceleration = PLAYER_DECELERATION

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.timer(dt)
        print(self.shoot_timer)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def timer(self, dt):
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def respawn(self):
        self.kill()
        Player.lives -= 1
        return Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

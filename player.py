from circleshape import CircleShape
import pygame
from constants import *
from game_objects import *

class Player(CircleShape):

    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = shots_group
        self.time = 0
    

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.time = max(0, self.time - dt)

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

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.time <= 0:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Start the shot at the front of the triangle
            shot_pos_x = self.position.x + (forward.x * self.radius)
            shot_pos_y = self.position.y + (forward.y * self.radius)
            new_shot = Shot(shot_pos_x, shot_pos_y, SHOT_RADIUS)
            velocity = pygame.Vector2(0, 1)
            velocity = velocity.rotate(self.rotation)
            velocity = velocity * PLAYER_SHOOT_SPEED  
            new_shot.velocity = velocity
            self.shots.add(new_shot)
            self.time = PLAYER_SHOOT_COOLDOWN
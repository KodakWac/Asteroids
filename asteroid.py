import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            vector1 = self.velocity.rotate(random_angle) * 1.2
            vector2 = self.velocity.rotate(-random_angle) * 1.2
            
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1
            

            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = vector2

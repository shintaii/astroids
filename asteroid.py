import circleshape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20.0, 50.0)
        print(f'oldv:{self.velocity}')
        vector_1 = self.velocity.rotate(split_angle)
        vector_2 = self.velocity.rotate(-split_angle)

        print(f'new_v1{vector_1}')

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vector_1 * 1.2
        print(f'mvec:{vector_1 * 1.2}')
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vector_2 * 1.2

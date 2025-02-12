import pymunk
import pygame
import random

class Ball:
    def __init__(self, space, position, radius=20, mass=1, elasticity=0.85):
        inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
        self.body = pymunk.Body(mass, inertia)
        self.body.position = position
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = elasticity
        self.shape.friction = 1.2
        self.color = (128, 128, 128)
        space.add(self.body, self.shape)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.body.position.x), int(self.body.position.y)),
            int(self.shape.radius)
        )
        
        
    @staticmethod
    def spawn(space):
        x = random.randint(115, 350)
        return Ball(space, (x, 200))
        
    
import pymunk
import pygame

class Ball:
    def __init__(self, x, y, radius, mass):
        self.radius = radius
        self.body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 0.8
        self.shape.friction = 0.5
        
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (128, 128, 128),
            (int(self.body.position.x), int(self.body.position.y)),
            self.radius
        )
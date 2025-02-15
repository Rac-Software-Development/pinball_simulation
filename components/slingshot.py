import pymunk
import pygame

class Slingshot:
    def __init__(self, space, start_pos, end_pos, elasticity=1.5, color=(255,255,255)):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, start_pos, end_pos, 5)
        self.shape.elasticity = elasticity
        self.shape.friction = 0.5
        self.shape.color =pygame.Color(*color)
        space.add(self.body, self.shape)

    
    def draw(self, screen):
        pygame.draw.line(screen, self.shape.color, self.shape.a, self.shape.b, 5)


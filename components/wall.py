import pymunk
import pygame

class Wall:
    def __init__(self, start, end, thickness=5, color=None):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, start, end, thickness)
        self.shape.elasticity = 0.7
        self.thickness = thickness
        self.color = color if color else pygame.Color("Black")
        self.start = start
        self.end = end
        
    def draw(self, screen):
        pygame.draw.line(
            screen, self.color, (int(self.start[0]), int(self.start[1])), (int(self.end[0]), int(self.end[1])), self.thickness
        )
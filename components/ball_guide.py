import pymunk
import pygame

class BallGuide:
    def __init__(self, space, start_pos, end_pos, width=5, color=(0,0,0)):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, start_pos, end_pos, width)
        self.shape.elasticity = 1.0
        self.shape.friction = 0.2
        space.add(self.body, self.shape)

        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = width
        self.color = color

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.start_pos, self.end_pos, self.width)



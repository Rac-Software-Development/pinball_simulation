import pymunk
import pygame

class Wall:
    def __init__(self, space, start_point, end_point, thickness=1.0, elasticity=0.7):
        self.shape = pymunk.Segment(space.static_body, start_point, end_point, thickness)
        self.shape.elasticity = elasticity
        space.add(self.shape)
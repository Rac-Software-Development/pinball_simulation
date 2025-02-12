import pymunk
import pygame
import pygame

class OuterLine: 
    def __init__(self, space, vertices, thickness=5.0, elasticity=0.8, color=(255, 255, 255)):
       self.color = color
       self.lines = []
       
       for i in range(len(vertices) - 1):
           segment = pymunk.Segment(
               space.static_body,
               vertices[i],
               vertices[i + 1],
               thickness
           )
           segment.elasticity = elasticity
           self.lines.append(segment)
           space.add(segment)
       
    def draw(self, screen):
        for line in self.lines:
            pygame.draw.line(
                screen,
                self.color,
                line.a,
                line.b,
                width=5
            )
    
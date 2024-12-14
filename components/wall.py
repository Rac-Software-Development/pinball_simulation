import pymunk
import pygame

class Wall:
    def __init__(self, points, thickness=5, color=None):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shapes = []
        self.thickness = thickness
        self.color = color if color else pygame.Color("black")

        for i in range(len(points) - 1):
            segment = pymunk.Segment(self.body, points[i], points[i + 1], thickness)
            segment.elasticity = 0.9
            self.shapes.append(segment)

        self.points = points

    def add_to_space(self, space):
        space.add(self.body)
        for shape in self.shapes:
            space.add(shape)

    def draw(self, screen):
        for i in range(len(self.points) - 1):
            pygame.draw.line(
                screen,
                self.color,
                (int(self.points[i][0]), int(self.points[i][1])),
                (int(self.points[i + 1][0]), int(self.points[i + 1][1])),
                self.thickness
            )

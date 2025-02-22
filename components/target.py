import pymunk
import pygame

class Target:
    def __init__(self, space, position, size, color=(255,0,0)):
        self.space = space
        self.size = size
        self.color = color

        # Create a body for the target
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = position

        # defines triangle vertices
        vertices = [(-size, size), (size, size), (0, -size)]

        # Create a polyglon shape for the target
        self.shape = pymunk.Poly(self.body, vertices)
        self.shape.friction = 0.9
        self.shape.collision_type = 2

        space.add(self.body, self.shape)

    def draw(self, screen):
        # draws the vertices
        vertices = [v.rotated(self.body.angle) + self.body.position for v in self.shape.get_vertices()]
        points = [(int(x), int(y)) for x, y in vertices]
        pygame.draw.polygon(screen, self.color, points)
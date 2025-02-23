import pymunk
import pygame

# bumper class
class Bumper:
    def __init__(self, space, position, radius=30, color=(255,255,255)):
        self.space = space
        self.radius = radius
        self.color = color
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = position
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 1.0
        self.shape.collision_type = 4
        self.space.add(self.body, self.shape)

    # draw the bumper
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (int(self.body.position.x), int(self.body.position.y)), self.radius)
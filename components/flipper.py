import pymunk
import pygame


class Flipper: 
    def __init__(self, space, position, length=100, angle=0, color=(0,0,255)):
        self.space = space
        self.position = pymunk.Vec2d(position)
        self.length = length
        self.angle = angle
        self.color = color
        
        # create the flipper body
        mass = 2
        moment = pymunk.moment_for_box(mass, (length, 20))
        self.body = pymunk.Body(mass, moment)
        self.body.position = self.position
        self.body.angle = self.angle
        
        # create the flipper shape
        self.shape = pymunk.Poly.create_box(self.body, (length, 20))
        self.shape.friction = 1
        self.space.add(self.body, self.shape)
        
        # create the pivot point
        pivot = pymunk.PivotJoint(self.space.static_body, self.body, self.position)
        self.space.add(pivot)
        
        # Create line that is attached to the flipper
        self.line_start = self.position
        self.line_end = self.position + pymunk.Vec2d(self.length, 0).rotated(self.angle)
        
    def rotate(self, angle_change):
        self.body.angle += angle_change
        
    def draw(self, screen):
        vertices = [self.body.position + v.rotated(self.body.angle) for v in self.shape.get_vertices()]
        pygame.draw.polygon(screen, self.color, vertices)

        pygame.draw.line(screen, (0,0,0), self.line_start, self.line_end, 2)

    def update_line(self):
        self.line_end =  self.position + pymunk.Vec2d(self.length, 0).rotated(self.body.angle)

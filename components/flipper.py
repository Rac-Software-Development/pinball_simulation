import pymunk
import pygame
import math

class Flipper:
    def __init__(self, space, position, length, angle=0, rotation_speed=5, color=pygame.Color("red"), is_left=True):
        self.position = position
        self.length = length
        self.angle = angle
        self.rotation_speed = rotation_speed
        self.color = color
        self.is_left = is_left
        self.initial_angle = angle

        self.body = pymunk.Body(10, 100)
        self.body.position = position
        self.body.angle = math.radians(angle)

        self.pivot_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = position

        half_length = length // 2
        self.shape = pymunk.Poly(self.body, [
            (-half_length, -10), (half_length, -10),
            (half_length, 10), (-half_length, 10)
        ])
        self.shape.elasticity = 0.5
        self.shape.friction = 1.0

        self.pivot = pymunk.PivotJoint(self.body, self.pivot_body, position)
        self.pivot.collide_bodies = False

        self.motor = pymunk.SimpleMotor(self.pivot_body, self.body, 0)
        self.motor.rate = 0

        space.add(self.body, self.shape, self.pivot, self.motor)

    def flip(self, is_flipping):
        if is_flipping:

            if self.is_left:
                self.motor.rate = math.radians(self.rotation_speed)
            else:
                self.motor.rate = -math.radians(self.rotation_speed)
        else:
            self.motor.rate = 0
            self.reset_position()  

    def reset_position(self):
        if abs(self.body.angle - math.radians(self.initial_angle)) > 0.01:
            angle_diff = self.initial_angle - math.degrees(self.body.angle)
            self.body.angle += angle_diff * 0.1          

    def draw(self, screen):
        vertices = [self.body.local_to_world(v) for v in self.shape.get_vertices()]

        vertices = [(int(v.x), int(v.y)) for v in vertices]
        if len(vertices) >= 3:
            pygame.draw.polygon(screen, self.color, vertices)
        else: 
            print("Error: Not enough vertices to draw the flipper.....")

import math 
import pygame
import pymunk

# flipper class
class Flipper:
    def __init__(self, space, position, is_left):
        self.space = space
        self.is_left = is_left

        
        width, height = 100, 20
        mass = 2
        moment = pymunk.moment_for_box(mass, (width, height))

        self.body = pymunk.Body(mass, moment)
        self.body.position = position
        self.body.angle = 0.0

        
        self.shape = pymunk.Poly.create_box(self.body, (100, 20))
        self.shape.elasticity = 0.5
        self.space.add(self.body, self.shape)


        pivot_offset = (-width / 2, 0) if is_left else (width / 2, 0)
        pivot_world = self.body.position + pivot_offset
        self.pivot = pymunk.PivotJoint(self.space.static_body, self.body, pivot_world)
        self.pivot.collide_bodies = False
        self.space.add(self.pivot)

        rest_angle = 0.0
        angle_range = math.radians(30) 
        min_angle = rest_angle - angle_range
        max_angle = rest_angle + angle_range
        self.limit_joint = pymunk.RotaryLimitJoint(self.space.static_body, self.body, min_angle, max_angle)
        space.add(self.limit_joint)

        self.spring = pymunk.DampedRotarySpring(self.space.static_body, self.body, rest_angle, stiffness=1000000, damping=10000)

        self.space.add(self.spring)

        self.target_angle = max_angle if is_left else min_angle

        self.motor = pymunk.SimpleMotor(self.space.static_body, self.body, 0)
        self.motor.max_force = 1500000
        self.motor_active = False
    
    # this function activates the flipper when the key is pressed
    def activate(self):
        if not self.motor_active:
            self.motor_active = True
            
            diff = self.target_angle - self.body.angle

            self.motor.rate = 10 if diff > 0 else -10
            self.space.add(self.motor)

    # this function deactivates the flipper when the key is released
    def deactivate(self):
        if self.motor_active:
            self.motor_active = False
            self.space.remove(self.motor)

    # draw the flipper
    def draw(self, screen):
        vertices = [self.body.local_to_world(v) for v in self.shape.get_vertices()]
        points = [(int(v.x), int(v.y)) for v in vertices]
        pygame.draw.polygon(screen, (0, 255, 0), points)
import pymunk
import pygame

class PhysicsEngine:
    def __init__(self, gravity=(0, 900), damping=0.99):
        self.space = pymunk.space()
        self.space.gravity = gravity
        self.space.damping = damping
        self.draw_options = None
        
    def add_obj(self, obj):
        if hasattr(obj, "body") and hasattr(obj, "shape"):
            self.space.add(obj.body, obj.shape)
        elif isinstance(obj, (pymunk.Body, pymunk.Shape)):
            self.space.add(obj)
        else:
            raise ValueError('Invalid object')
        
    def remove_obj(self, obj):
        if hasattr(obj, "body") and hasattr(obj, "shape"):
            self.space.remove(obj.body, obj.shape)
        elif isinstance(obj, (pymunk.Body, pymunk.Shape)):
            self.space.remove(obj)
        else:
            raise ValueError('Invalid object')
        
    def step(self, dt):
        self.space.step(dt)        
    
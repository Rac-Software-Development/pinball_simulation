import pymunk
import pygame

class PhysicsEngine:
    def __init__(self):
        self.space = pymunk.space()
        self.space.gravity = (0, 900)
        
    def step(self, dt):
        self.step(dt)
import pymunk

class Ball:
    def __init__(self, x, y, radius):
        self.body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = elasticity
        self.shape.friction = friction
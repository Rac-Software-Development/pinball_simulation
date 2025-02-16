import pymunk
import pygame

class Slingshot:
   def __init__(self, space, pivot, is_left, elasticity=1.8, color=(255, 255, 255)):
         self.space = space
         self.is_left = is_left
         self.color = pygame.Color(*color)
         
         # triangle shape
         offset = -50 if is_left else 50
         base = 80
         height = 40

         self.points = [
              (pivot[0] - base // 2, pivot[1]),
              (pivot[0] + base // 2, pivot[1]),
              (pivot[0] + offset, pivot[1] - height)
         ]

         self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
         self.shape = pymunk.Poly(self.body, self.points)
         self.shape.elasticity = elasticity
         self.shape.friction = 0.5
         self.shape.collision_type = 2

         space.add(self.body, self.shape)

   def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.points)



import pygame
import pymunk
from components.ball import Ball


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Dylan\'s Pinball simulation')
    
    
    space = pymunk.Space()
    space.gravity = (0, 900)
    
    ball = Ball(300, 100, radius=10, mass=1)
    
    
    space.add(ball.body, ball.shape)
    
    
    clock = pygame.time.Clock()
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        screen.fill((0, 0, 0))
        
        ball.draw(screen)
        space.step(1 / FPS)
        
        pygame.display.flip()
        clock.tick(FPS)

        
    pygame.quit()
    
if __name__ == "__main__":
    main()
    
    



    

        
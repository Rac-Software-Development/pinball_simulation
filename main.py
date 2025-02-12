import pygame
import pymunk
import pymunk.pygame_util
from components.ball import Ball
from components.outer_lines import OuterLine
from components.flipper import Flipper
from components.bumper import Bumper
from components.ball_guide import BallGuide

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
FPS = 60

def create_outer_lines(space):
   return [
       # left line
       OuterLine(space, [
           (50, 850), # bottom left
           (50, 50), # top left
           (300, 10), # diagonal line to top center
       ], color=(255, 255, 255)),
       
       # right line
       OuterLine(space, [
           (550, 850), # bottom right
           (550, 50), # top right
           (300, 10) # diagonal line to top center
       ], color=(255, 255, 255)),
       
       # bottom line
       OuterLine(space, [
           (200, 850),
           (50, 850),
       ], color=(255, 255, 255)),

        # bottom line
       OuterLine(space, [
           (550, 850),
           (450, 850),
       ], color=(255, 255, 255)),
   ]
   
    

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Dylan's Pinball simulation")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0, 600)
    

    ball = Ball(space, (150, 100), radius=10, mass=2, elasticity=0.85)
    ball.body.velocity = pymunk.Vec2d(0, 50)


    outer_lines = create_outer_lines(space)

    ball_guides = [
        BallGuide(space, (175, 750), (100, 675)), # left guide
        BallGuide(space, (425, 750), (500, 675)) # right guide
    ]

    left_flipper = Flipper(space, (230, 750), is_left=True)
    right_flipper = Flipper(space, (370, 750), is_left=False)

    bumpers = [
        Bumper(space, (200, 600), color=(255, 255, 255)),
        Bumper(space, (400, 600), color=(255, 255, 255)),
    ]

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left_flipper.activate()
        else:
            left_flipper.deactivate()
        

        if keys[pygame.K_RIGHT]:
            right_flipper.activate()
        else:
            right_flipper.deactivate()

        screen.fill(pygame.Color("black"))

        ball.draw(screen)

        for line in outer_lines:
            line.draw(screen)

        for guide in ball_guides:
            guide.draw(screen)

        for bumper in bumpers:
            bumper.draw(screen)

        
        left_flipper.draw(screen)
        right_flipper.draw(screen)
        
        
        
        

        space.step(1 / FPS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

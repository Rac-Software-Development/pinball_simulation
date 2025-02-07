import pygame
import pymunk
import pymunk.pygame_util
from components.ball import Ball
from components.outer_lines import OuterLine
from components.flipper import Flipper
from components.bumper import Bumper

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
FPS = 60

def create_outer_lines(space):
   return [
       OuterLine(space, [
           (50, 850),
           (50, 50),
           (300, 10),
       ], color=(255, 0, 0)),
       
       OuterLine(space, [
           (550, 850),
           (550, 50),
           (300, 10)
       ], color=(255, 0, 0)),
       
       OuterLine(space, [
           (200, 850),
           (50, 850),
       ], color=(255, 0, 0)),
       
       OuterLine(space, [
           (550, 850),
           (450, 850),
       ], color=(255, 0, 0)),
   ]
   
    

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Dylan's Pinball simulation")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0, 900)
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    ball = Ball(space, (100, 100), radius=10, mass=1)
    ball.body.velocity = pymunk.Vec2d(0, 100)


    outer_lines = create_outer_lines(space)

    left_flipper = Flipper(space, (150, 700), is_left=True)
    right_flipper = Flipper(space, (450, 700), is_left=False)

    bumpers = [
        Bumper(space, (200, 600)),
        Bumper(space, (400, 600))
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

        screen.fill(pygame.Color("white"))


        for line in outer_lines:
            line.draw(screen)

        for bumper in bumpers:
            bumper.draw(screen)

        
        left_flipper.draw(screen)
        right_flipper.draw(screen)
        
        
        
        space.debug_draw(draw_options)

        space.step(1 / FPS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

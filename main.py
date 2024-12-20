import pygame
import pymunk
import pymunk.pygame_util
from components.ball import Ball
from components.wall import Wall
from components.flipper import Flipper

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
FPS = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Dylan's Pinball simulation")
    clock = pygame.time.Clock()
    run = True

    space = pymunk.Space()
    space.gravity = (0, 900)
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    ball = Ball(300, 100, radius=10, mass=1)
    ball.body.velocity = pymunk.Vec2d(0, 100)
    space.add(ball.body, ball.shape)

    wall_points = [
        Wall(space, (150, 500), (50, 50)),
        Wall(space, (450, 800), (550, 50)),
        Wall(space, (50, 50), (300, 0)),
        Wall(space, (300, 0), (550, 50)),
        Wall(space, (300, 180), (400, 200))
    ]



    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        

        screen.fill(pygame.Color("white"))
        space.debug_draw(draw_options)

        ball.draw(screen)
        space.step(1 / FPS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

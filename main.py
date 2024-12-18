import pygame
import pymunk
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

    space = pymunk.Space()
    space.gravity = (0, 800)

    ball = Ball(300, 100, radius=10, mass=1)
    ball.body.velocity = pymunk.Vec2d(0, 100)
    space.add(ball.body, ball.shape)

    wall_points = [
        (50, 850), (50, 700), (30, 500), (50, 300), (100, 200),
        (200, 100), (300, 50), (400, 100), (500, 200),
        (550, 300), (570, 500), (550, 700), (550, 850)
    ]
    outer_wall = Wall(wall_points, thickness=5, color=pygame.Color("black"))
    outer_wall.add_to_space(space)

    ramp_points = [
        (200, 700), 
        (400, 500)
    ]
    ramp = Wall(ramp_points, thickness=5, color=pygame.Color("blue"))

    for shape in ramp.shapes:
        shape.elasticity = 0.8
        shape.friction = 0.4
    ramp.add_to_space(space)

    left_flipper = Flipper(space, position=(125, 800), length=120, is_left=True)
    right_flipper = Flipper(space, position=(475, 800), length=120, is_left=False)

    clock = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left_flipper.flip(True)
        else:
            left_flipper.flip(False)

        if keys[pygame.K_RIGHT]:
            right_flipper.flip(True)
        else:
            right_flipper.flip(False)

        screen.fill(pygame.Color("white"))

        ball.draw(screen)
        outer_wall.draw(screen)
        ramp.draw(screen)
        left_flipper.draw(screen)
        right_flipper.draw(screen)

        space.step(1 / FPS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

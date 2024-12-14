import pygame
import pymunk
from components.ball import Ball
from components.wall import Wall


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
FPS = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Dylan's Pinball simulation")

    space = pymunk.Space()
    space.gravity = (0, 900)

    ball = Ball(300, 100, radius=10, mass=1)
    space.add(ball.body, ball.shape)

    

    wall_points = [
        (50, 850), (50, 700), (30, 500), (50, 300), (100, 200),
        (200, 100), (300, 50), (400, 100), (500, 200),
        (550, 300), (570, 500), (550, 700), (550, 850)
    ]
    outer_wall = Wall(wall_points, thickness=5, color=pygame.Color("black"))
    outer_wall.add_to_space(space)

    clock = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(pygame.Color("white"))
        ball.draw(screen)
        outer_wall.draw(screen)
        

        space.step(1 / FPS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

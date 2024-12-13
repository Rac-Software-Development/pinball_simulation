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

    wall_top = Wall((50, 50), (550, 50), thickness=5, color=pygame.Color("black"))
    wall_left = Wall((50, 50), (50, 850), thickness=5, color=pygame.Color("black"))
    wall_right = Wall((50, 50), (550, 850), thickness=5, color=pygame.Color("black"))

    space.add(wall_top.body, wall_top.shape)
    space.add(wall_left.body, wall_left.shape)
    space.add(wall_right.body, wall_right.shape)

    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        clock.tick(FPS)

        screen.fill(pygame.Color("white"))
        ball.draw(screen)
        wall_top.draw(screen)
        wall_left.draw(screen)
        wall_right.draw(screen)
        space.step(1 / FPS)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

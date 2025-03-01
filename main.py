import pygame
import pymunk
import pymunk.pygame_util
from components.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from components.ball import Ball
from components.outer_lines import OuterLine
from components.flipper import Flipper
from components.bumper import Bumper
from components.ball_guide import BallGuide
from components.slingshot import Slingshot
from components.target import Target
from components.score_board import ScoreBoard




def create_outer_lines(space):
   return [
       # left line slighly diagonal to the top center
       OuterLine(space, [
           (50, 850), # bottom left
           (50, 50), # top left
           (300, 10), # diagonal line to top center
       ], color=(255, 255, 255)),
       
       # right line slighly diagonal to the top center
       OuterLine(space, [
           (550, 850), # bottom right
           (550, 50), # top right
           (300, 10) # diagonal line to top center
       ], color=(255, 255, 255)),
       
       # bottom left section of the bottom line
       OuterLine(space, [
           (200, 850), # middle bottom
           (50, 850), # bottom left
       ], color=(255, 255, 255)),

        # bottom right section of the bottom line
       OuterLine(space, [
           (550, 850), # bottom right
           (450, 850), # slightly left of the middle bottom
       ], color=(255, 255, 255)),
   ]
   
    
# the main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Dylan's Pinball simulation")
    clock = pygame.time.Clock()

    highscore = 0

    # create the space
    space = pymunk.Space()
    space.gravity = (0, 600)
    
    # create the ball
    ball = Ball.spawn(space, radius=10)
    ball.body.velocity = pymunk.Vec2d(0, 50)

    # create the outer lines
    outer_lines = create_outer_lines(space)

    # create the line that guides the ball to the flippers
    ball_guides = [
        BallGuide(space, (175, 750), (50, 675)), # left guide
        BallGuide(space, (425, 750), (550, 675)) # right guide
    ]

    # create the slingshots
    slingshots = [
        Slingshot(space, (200, 620), is_left=True),
        Slingshot(space, (400, 620), is_left=False)
    ]


    # create the flippers
    left_flipper = Flipper(space, (230, 750), is_left=True)
    right_flipper = Flipper(space, (370, 750), is_left=False)

    # create the bumpers
    bumpers = [
        Bumper(space, (200, 300), color=(255, 255, 255)),
        Bumper(space, (400, 400), color=(255, 255, 255)),
        Bumper(space, (300, 200), color=(255, 255, 255)),
        Bumper(space, (350, 500), color=(255, 255, 255))
    ]

    
    # create the targets
    targets = [
        Target(space, (300, 500), 20),
        Target(space, (250, 400), 25),
        Target(space, (150, 250), 20),
        Target(space, (450, 200), 25),
        Target(space, (300, 100), 20)
    ]

    scoreboard = ScoreBoard(font_size=36, position=(10, 5))

    def hits_target(arbiter, space, data):
        scoreboard.increase_score(10)
        print("Target hit! Score:", scoreboard.score)
        return True
    
    handler = space.add_collision_handler(1, 2)
    handler.begin = hits_target

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
        ball.body.velocity = ball.body.velocity * ball.damping

        for line in outer_lines:
            line.draw(screen)

        for guide in ball_guides:
            guide.draw(screen)

        for bumper in bumpers:
            bumper.draw(screen)
        
        for sling in slingshots:
            sling.draw(screen)

        for target in targets:
            target.draw(screen)

        
        left_flipper.draw(screen)
        right_flipper.draw(screen)

        scoreboard.draw(screen)

        if ball.body.position.y > SCREEN_HEIGHT:
            scoreboard.decrease_life()
            print(f"remaining lives: {scoreboard.lives}")
            if scoreboard.lives > 0:
                ball = Ball.spawn(space, radius=10)
            else:
                from components.game_over import game_over_screen
                if scoreboard.score > highscore:
                    highscore = scoreboard.score
                choice = game_over_screen(screen, scoreboard.score, highscore)
                if choice == "restart":
                    main()
                else:
                    run = False
        
        
        space.step(1 / FPS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

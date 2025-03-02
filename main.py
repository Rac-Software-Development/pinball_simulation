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
from mqtt_client import send_score




class PinballGame:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 600)
        self.ball = self.create_ball()
        self.outer_lines = self.create_outer_lines()
        self.ball_guides = self.create_ball_guides()
        self.slingshots = self.create_slingshots()
        self.left_flipper, self.right_flipper = self.create_flippers()
        self.bumpers = self.create_bumpers()
        self.targets = self. create_targets()
        self.scoreboard = ScoreBoard(font_size=36, position=(10, 5))
        self.highscore = 0
        self.setup_collision_handlers()

    # creates the ball and sets the velocity
    def create_ball(self):
        ball = Ball.spawn(self.space, radius=10)
        ball.body.velocity = pymunk.Vec2d(0, 50)
        return ball
    
    # creates the outer lines of the pinball table
    def create_outer_lines(self):
        return [
            OuterLine(self.space, [(50, 850), (50, 50), (300, 10)], color=(255, 255, 255)),
            OuterLine(self.space, [(550, 850), (550, 50), (300, 10)], color=(255, 255, 255)),
            OuterLine(self.space, [(200, 850), (50, 850)], color=(255, 255, 255)),
            OuterLine(self.space, [(550, 850), (450, 850)], color=(255, 255, 255)),
        ]
    
    # creates the guides for the ball to the flipper
    def create_ball_guides(self):
        return [
            BallGuide(self.space, (175, 750), (50, 675)),
            BallGuide(self.space, (425, 750), (550, 675))
        ]
    
    # creates the slingshots, also sets the location
    def create_slingshots(self):
        return [
            Slingshot(self.space, (200, 620), is_left=True),
            Slingshot(self.space, (400, 620), is_left=False)
        ]
    
    # creates the flippers, also sets the location
    def create_flippers(self):
        left_flipper = Flipper(self.space, (230, 750), is_left=True)
        right_flipper = Flipper(self.space, (370, 750), is_left=False)
        return left_flipper, right_flipper
    
    # creates the bumpers, also sets the location and color
    def create_bumpers(self):
        return [
            Bumper(self.space, (200, 300), color=(255, 255, 255)),
            Bumper(self.space, (400, 400), color=(255, 255, 255)),
            Bumper(self.space, (300, 200), color=(255, 255, 255)),
            Bumper(self.space, (350, 500), color=(255, 255, 255))
        ]
    
    # creates the targets, also sets the location and size
    def create_targets(self):
        return [
            Target(self.space, (100, 300), 20),
            Target(self.space, (450, 200), 25),
            Target(self.space, (300, 100), 20)
        ]
    
    # setup collision handlers
    def setup_collision_handlers(self):
        def hits_target(arbiter, space, data):
            self.scoreboard.increase_score(10)
            send_score(self.scoreboard.score)
            return True
        
        handler = self.space.add_collision_handler(1, 2)
        handler.begin = hits_target
    
    def game_over(self, screen):
        from components.game_over import game_over_screen
        if self.scoreboard.score > self.highscore:
            self.highscore = self.scoreboard.score
        choice = game_over_screen(screen, self.scoreboard.score, self.highscore)
        return choice

def handle_user_input(keys, left_flipper, right_flipper):
    if keys[pygame.K_LEFT]:
            left_flipper.activate()
    else:
            left_flipper.deactivate()
        

    if keys[pygame.K_RIGHT]:
            right_flipper.activate()
    else:
            right_flipper.deactivate()
    
    

# the main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Dylan's Pinball simulation")
    clock = pygame.time.Clock()

    # create the game
    game = PinballGame()

    # run the game
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # handle user input
        keys = pygame.key.get_pressed()
        handle_user_input(keys, game.left_flipper, game.right_flipper)

        screen.fill(pygame.Color("black"))

        game.ball.draw(screen)
        # Apply damping to the ball
        game.ball.body.velocity = game.ball.body.velocity * game.ball.damping

        for line in game.outer_lines:
            line.draw(screen)

        for guide in game.ball_guides:
            guide.draw(screen)

        for bumper in game.bumpers:
            bumper.draw(screen)
        
        for sling in game.slingshots:
            sling.draw(screen)

        for target in game.targets:
            target.draw(screen)

        
        game.left_flipper.draw(screen)
        game.right_flipper.draw(screen)

        game.scoreboard.draw(screen)

        # check if the ball is out of bounds and either respawns or ends the game
        if game.ball.body.position.y > SCREEN_HEIGHT:
            game.scoreboard.decrease_life()
            print(f"remaining lives: {game.scoreboard.lives}")
            if game.scoreboard.lives > 0:
                game.ball = game.create_ball()
            else:
                choice = game.game_over(screen)
                if choice == "restart":
                    game.__init__()
                else:
                    run = False
        
        
        game.space.step(1 / FPS)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

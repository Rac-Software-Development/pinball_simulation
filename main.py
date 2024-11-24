import pygame
import pymunk
import pymunk.pygame_util



pygame.init()

WIDTH, HEUGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEUGHT))



def draw(space, window, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()


def create_ball(space, radius, mass):
    body = pymunk.Body()
    body.position = (100, 300)
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (0, 0, 255)
    space.add(body, shape)
    return shape
    
    

def run(window, WIDTH, HEUGHT):
    running = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps
    
    space = pymunk.Space()
    space.gravity = (0, 900)
    
    ball = create_ball(space, 20, 5)
    
    draw_options = pymunk.pygame_util.DrawOptions(window)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True
                break
                
        draw(space, window, draw_options)
        space.step(dt)
        clock.tick(fps)
        
    pygame.quit()
    
if __name__ == "__main__":
    run(window, WIDTH, HEUGHT)
        
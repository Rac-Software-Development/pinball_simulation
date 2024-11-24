import pygame
import pymunk
import pymunk.pygame_util



pygame.init()

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))



def draw(space, window, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()


def create_ball(space, radius, mass):
    body = pymunk.Body()
    body.position = (100, 300)
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (0, 0, 255, 255)
    space.add(body, shape)
    return shape

def create_line(space, start, end):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, start, end, 5)
    shape.color = (0, 0, 0, 255)
    space.add(body, shape)
    return shape
    
    

def run(window):
    running = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps
    
    space = pymunk.Space()
    space.gravity = (0, 900)
    
    ball = create_ball(space, 20, 5)
    
    line = create_line(space, (0, 400), (WIDTH - 200, 600))
    
    draw_options = pymunk.pygame_util.DrawOptions(window)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
                
        draw(space, window, draw_options)
        space.step(dt)
        clock.tick(fps)
        
    pygame.quit()
    
if __name__ == "__main__":
    run(window)
        
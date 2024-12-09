import pytest
import sys
sys.path.insert(0, "C:/pinball_simulation/pinball_simulation/")
from components.ball import Ball
import pymunk

# creating a pymunk space for testing
@pytest.fixture
def space():
    return pymunk.Space()

# tests the initialization of the ball object
def test_ball_init(space):
    ball = Ball(300, 400, radius=10, mass=1)
    assert ball.body.position == (300, 400)
    assert ball.radius == 10

# tests physical capabilities of the ball
def test_ball_collision(space):
    ball = Ball(300, 400, radius=10, mass=1)
    assert ball.shape.elasticity == 0.8
    assert ball.shape.friction == 0.5
    
# tests the ball adding to the space
def test_ball_added_to_space(space):
    ball = Ball(300, 400, radius=10, mass=1)
    space.add(ball.body, ball.shape)
    assert ball.body in space.bodies
    assert ball.shape in  space.shapes

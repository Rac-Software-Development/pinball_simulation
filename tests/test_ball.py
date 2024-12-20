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
    ball = Ball(space, (300, 400))
    assert ball.body.position.x == 300
    assert ball.body.position.y == 400
    assert isinstance(ball.body, pymunk.Body)
    assert isinstance(ball.shape, pymunk.Circle)

# tests physical capabilities of the ball
def test_ball_spawn(space):
    ball = Ball.spawn(space)
    assert isinstance(ball, Ball)
    assert 115 <= ball.body.position.x <= 350
    assert ball.body.position.y == 200

import pytest
import pymunk
import sys
sys.path.insert(0, "C:/Users/dylsa/pinball_simulation-1/")
from components.bumper import Bumper
from components.ball import Ball


@pytest.fixture
def space(): 
    return pymunk.Space()

@pytest.fixture
def ball(space):
    ball = Ball(space, (300, 400))
    ball.body.velocity = pymunk.Vec2d(0, 100)
    return ball

@pytest.fixture
def bumper(space):
    return Bumper(space, ())

def test_bumper_initialization(bumper):
    assert bumper.body.position == (300, 400)
    assert bumper.radius == 30
    assert bumper.shape.elasticity == 1.0

def test_ball_collide_with_bumper(space, ball, bumper):
    ball.body.velocity == pymunk.Vec2d(50, 0)

    space.step(1 / 60)

    assert ball.body.velocity.x != 50
    assert ball.body.velocity.y != 0

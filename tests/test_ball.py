import pytest
import sys
sys.path.insert(0, "C:/pinball_simulation/pinball_simulation/")
from components.ball import Ball
import pymunk

def space():
    return pymunk.Space()

def test_ball_init(space):
    ball = Ball(300, 400, radius=10, mass=1)
    assert ball.body.position == (300, 400)
    assert ball.radius == 10

def test_ball_collision(space):
    ball = Ball(300, 400, radius=10, mass=1)
    assert ball.shape.elasticity == 0.8
    assert ball.shape.friction == 0.5

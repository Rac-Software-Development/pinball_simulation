import pytest
import sys
sys.path.insert(0, "C:/pinball_simulation/pinball_simulation/")
from components.ball import Ball
import pymunk

def space():
    return pymunk.Space()

def test_ball_init(space):
    position = (100, 300)
    ball = Ball(space, position)
    
    assert ball.body.position == position
    assert ball.shape.radius == 15
    assert ball.shape.elasticity == 0.8
    
        
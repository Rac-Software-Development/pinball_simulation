import pytest
import sys
sys.path.insert(0, "C:/pinball_simulation/pinball_simulation/")
from components.flipper import Flipper
import pymunk

@pytest.fixture
def space():
    space = pymunk.Space()
    space.gravity = (0, 0)
    return space

def test_flipper_making(space):
    flipper = Flipper(space, (150, 700), length=100, angle=0)
    
    assert flipper.body.position == pymunk.Vec2d(150, 700)
    
    assert flipper.length == 100
    
    assert flipper.body.angle == 0
    
def test_flipper_rotation(space):
    flipper = Flipper(space, (150, 700), length=100, angle=0)
    
    initial_angle = flipper.body.angle
    flipper.rotate(3.14 / 4)
    
    assert flipper.body.angle == pytest.approx(initial_angle + 3.14 / 4, rel=1e-2)
    
def test_flipper_line_update(space):
    flipper = Flipper(space, (150, 700), length=100, angle=0)
    
    initial_line_end = flipper.line_end
    flipper.rotate(3.14 / 4)
    
    assert flipper.line_end != initial_line_end
    assert flipper.line_end == pytest.approx(
        flipper.position + pymunk.Vec2d(100, 0).rotated(flipper.body.angle),
        rel=1e-2
    )
    
    
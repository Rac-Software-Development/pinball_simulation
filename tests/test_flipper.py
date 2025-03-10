import pytest
import sys
sys.path.insert(0, "C:/Users/dylsa/pinball_simulation-1/")
from components.flipper import Flipper
import pymunk

@pytest.fixture
def space():
    space = pymunk.Space()
    space.gravity = (0, 0)
    return space

# tests if the flipper is created at the correct position
def test_flipper_making(space):
    flipper = Flipper(space, (150, 700), is_left=True)
    
    assert flipper.body.position == pytest.approx(pymunk.Vec2d(150, 700), rel=1e-3)
    assert flipper.body.angle == 0.0
    assert flipper.is_left is True

# tests if the flipper rotates in the correct direction
def test_flipper_rotation(space):
    flipper = Flipper(space, (150, 700), is_left=True)

    initial_angle = flipper.body.angle
    print(f"initial angle: {initial_angle}")

    flipper.activate()

    # step simulation and check if flipper rotates in the correct direction
    for _ in range(10):
        space.step(1/60)

    new_angle = flipper.body.angle
    print(f"new_angle after activation: {new_angle}")

    # expect the left flipper  to rotate counterclockwise and the right flipper clockwise
    if flipper.is_left:
        assert new_angle < initial_angle, f"Left flipper should rotate counterclockwise. expected < {initial_angle}, got {new_angle}"
    else:
        assert new_angle > initial_angle, f"Right flipper should rotate clockwise. expected > {initial_angle}, got {new_angle}"

def test_flipper_deactivation(space):
    flipper = Flipper(space, (150, 700), is_left=True)

    # activate the flipper and step simulation
    flipper.activate()
    for _ in range(10):
        space.step(1/60)

    # deactivate the flipper and step again
    flipper.deactivate()
    for _ in range(10):
        space.step(1/60)


# tests if the pivot point moves correctly when the flipper is activated
def test_flipper_line_update(space):
    flipper = Flipper(space, (150, 700), is_left=True)
    expected_pivot = pymunk.Vec2d(150, 700) + pymunk.Vec2d(-50, 0)
    
    # activate the flipper and step simulation
    flipper.activate()
    for _ in range(10):
        space.step(1/60)

    actual_pivot = flipper.pivot.anchor_a
    assert actual_pivot == pytest.approx(expected_pivot, rel=1e-2), f"pivot point moved! expected {expected_pivot}, got {actual_pivot}"
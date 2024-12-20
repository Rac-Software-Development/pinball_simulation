import pytest
import pymunk
import sys
sys.path.insert(0, "C:/pinball_simulation/pinball_simulation/")
from components.wall import Wall


@pytest.fixture
def space():
    return pymunk.Space()


def test_wall_initialization(space):
    wall = Wall(space, (100, 100), (200, 200))
    assert isinstance(wall.shape, pymunk.Segment)
    assert wall.shape.elasticity == 0.7
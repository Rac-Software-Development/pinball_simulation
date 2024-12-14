import pytest
import pygame
import pymunk
import sys
sys.path.insert(0, "C:/pinball_simulation/pinball_simulation/")
from components.wall import Wall


@pytest.fixture
def mock_space():
    space = pymunk.Space()
    return space

@pytest.fixture
def mock_screen():
    pygame.init()
    screen = pygame.Surface((600, 900))
    return screen

def test_wall_making(mock_space):
    wall_points = [
        (50, 850),
        (50, 700),
        (30, 500),
        (50, 300),
        (100, 200),
        (200, 100),
        (300, 50),
        (400, 100),
        (500, 200),
        (550, 300),
        (570, 500),
        (550, 700),
        (550, 850),
    ]
    wall = Wall(wall_points, thickness=5, color=(0, 0, 0))
    
    assert len(wall.shapes) == len(wall_points) - 1
    assert wall.thickness == 5
    assert wall.color == (0, 0, 0)

def test_wall_to_space(mock_space, mock_screen):
    wall_points = [(50, 850), (50, 700), (30, 500), (50, 300), (100, 200)]
    wall = Wall(wall_points, thickness=5, color=pygame.Color("black"))
    wall.add_to_space(mock_space)
    
    for shape in wall.shapes:
        assert shape in mock_space.shapes
    
    try:
        wall.draw(mock_screen)
    except Exception as e:
        pytest.fail(f"wall drawing rasied an exception: {e}")

import pytest
import sys
sys.path.insert(0, "C:/pinball_simulation/pinball_simulation/")
from components.flipper import Flipper
import pygame
import pymunk

def mock_space():
    space = pymunk.Space()
    return space


def flipper(mock_space):
    flipper = Flipper(position=(300, 750), length=100, angle=0, rotation_speed=10)
    mock_space.add(flipper.body, flipper.shape)
    return flipper        

def test_flipper_rotation(flipper):
    initial_angle = flipper.body.angle
    flipper.rotate("clockwise")
    assert flipper.body.angle > initial_angle
    
    initial_angle = flipper.body.angle
    flipper.rotate("counterclockwise")
    assert flipper.body.angle < initial_angle
    
def test_flipper_draw(flipper, mock_screen):
    with pytest.mock.patch("pygame.draw.polyglon") as mock_draw:
        flipper.draw(mock_screen)
        mock_draw.assert_called_once()
        
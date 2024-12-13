import pytest
import sys
sys.path.insert(0, "C:/pinball_simulation/pinball_simulation/")
from components.wall import Wall



@pytest.fixture
def wall():
    return Wall((50, 50), (550, 50), thickness=5, color=(0, 0, 0))

def test_wall_init(wall):
    assert wall.start == (50, 50)
    assert wall.end == (550, 50)
    assert wall.thickness == 5
    assert wall.color == (0, 0, 0)
    
def test_wall_elasticity(wall):
    assert wall.shape.elasticity == 0.7

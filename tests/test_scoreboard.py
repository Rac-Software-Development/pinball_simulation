import pytest
import sys
sys.path.insert(0, "C:/Users/dylsa/pinball_simulation-1/")
from components.score_board import ScoreBoard

@pytest.fixture
def scoreboard():
    return ScoreBoard()

def test_initial_score(scoreboard):
    assert scoreboard.score == 0 # initial score value should be 0

def test_increase_score(scoreboard):
    scoreboard.increase_score(10)
    assert scoreboard.score == 10 # score should be 10 after increasing by 10

    scoreboard.increase_score(5)
    assert scoreboard.score == 15 # Score should be 15 after increasing by 5

def test_multiple_increases(scoreboard):
    scoreboard.increase_score(10)
    scoreboard.increase_score(20)
    scoreboard.increase_score(30)

    assert scoreboard.score == 60


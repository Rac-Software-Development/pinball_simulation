import pytest
import sys
sys.path.insert(0, "C:/pinball_simulation/pinball_simulation/")
from components.physics_eng import PhysicsEngine

def test_physics_engine_init():
    engine = PhysicsEngine()
    assert engine.space.gravity == (0, 900)

def test_physics_engine():
    engine = PhysicsEngine()
    time_init = engine.space.time
    engine.step(1/ 60)
    assert engine.space.time > time_init

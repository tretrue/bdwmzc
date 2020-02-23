import pytest
import System
import TA


# Testing to see if the program can handle creating a TA with an invalid name
def test_ta(grading_system):
    name = ''
    new_TA = TA.TA(name, grading_system.users, grading_system.courses)
    assert new_TA


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

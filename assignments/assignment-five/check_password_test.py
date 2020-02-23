import pytest
import System


# Tests if the program can check a password
def test_password(grading_system):
    username = 'akend3'
    password = 'TestingIncorrect'
    test1 = grading_system.check_password(username, password)

    username = 'akend3'
    password = '123454321'
    test2 = grading_system.check_password(username, password)

    if not test1 and test2:
        assert True, "Correct password passed and incorrect password failed"
    else:
        assert False, "Password check failed"


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

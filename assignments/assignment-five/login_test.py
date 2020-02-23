import pytest
import System


def test_login(grading_system):
    username = 'akend3'
    password = '123454321'
    if grading_system.login(username, password) is None:
        assert True
    else:
        assert False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

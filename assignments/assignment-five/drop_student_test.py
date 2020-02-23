import pytest
import System
import Professor


def test_student(prof_system):
    name = 'yted91'
    course = 'software_engineering'
    assert prof_system.drop_student(name, course)


@pytest.fixture
def prof_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    name = 'goggins'
    professorSystem = Professor.Professor(name, gradingSystem.users, gradingSystem.courses)
    return professorSystem

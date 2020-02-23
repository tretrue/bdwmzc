import pytest
import Professor
import System


# Testing to see if we are able to add a non-existing student to a database
def test_student(prof_system):
    name = ''
    course = 'databases'
    test_empty = prof_system.add_student(name, course)

    assert not test_empty


@pytest.fixture
def prof_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    name = 'goggins'
    professorSystem = Professor.Professor(name, gradingSystem.users, gradingSystem.courses)
    return professorSystem

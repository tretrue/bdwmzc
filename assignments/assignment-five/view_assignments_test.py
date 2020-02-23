import pytest
import System
import Student


def test_assignments(student_system):
    course = 'cloud_computing'
    assert student_system.view_assignments(course)


@pytest.fixture
def student_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    name = 'yted91'
    studentSystem = Student.Student(name, gradingSystem.users, gradingSystem.courses)
    return studentSystem

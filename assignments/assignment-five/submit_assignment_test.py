import pytest
import System
import Student


def test_submit(student_system):
    course = 'cloud_computing'
    assignment_name = 'assignment2'
    submission = 'Blah Blah Blah'
    submission_date = '01/01/20'
    if student_system.submit_assignment(course, assignment_name, submission, submission_date) is None:
        assert True
    else:
        assert False


@pytest.fixture
def student_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    name = 'yted91'
    studentSystem = Student.Student(name, gradingSystem.users, gradingSystem.courses)
    return studentSystem

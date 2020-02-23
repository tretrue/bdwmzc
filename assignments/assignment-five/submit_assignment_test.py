import pytest
import System
import Student


def test_submit(student_system):
    course = 'cloud_computing'
    assignment_name = 'assignment3'
    submission = 'Blah Blah Blah'
    submission_date = '01/01/20'
    assert student_system.submit_assignment(course, assignment_name, submission, submission_date)


@pytest.fixture
def student_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    name = 'yted91'
    studentSystem = Student.Student(name, gradingSystem.users, gradingSystem.courses)
    return studentSystem

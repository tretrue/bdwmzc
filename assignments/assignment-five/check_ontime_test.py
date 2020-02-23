import pytest
import System
import Student


def test_ontime(student_system):
    due_date = '04/01/20'
    submission_date = '03/01/20'
    submission_date2 = '05/01/20'
    if student_system.check_ontime(submission_date, due_date) and not student_system.check_ontime(submission_date2, due_date):
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

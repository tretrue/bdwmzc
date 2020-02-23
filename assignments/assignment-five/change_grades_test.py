import pytest
import Staff


def test_grades(staff_system):
    username = 'akend3'
    course = 'comp_sci'
    assignment = "assignment1"
    assert staff_system.change_grade(username, course, assignment, 50)


@pytest.fixture
def staff_system():
    staffSystem = Staff.Staff()
    return staffSystem

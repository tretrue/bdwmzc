import pytest
import Staff


# Testing if we can add an assignment with an invalid course to the database
def test_assignment(staff_system):
    assignment_name = 'assignment99'
    due_date = '1/1/70'
    course = ''
    test_course = staff_system.create_assignment(assignment_name, due_date, course)
    assert not test_course


@pytest.fixture
def staff_system():
    staffSystem = Staff.Staff()
    return staffSystem


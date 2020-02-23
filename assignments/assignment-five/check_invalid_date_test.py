import pytest
import Staff


# Test to see if we are able to add an invalid due date to the database
def test_assignment(staff_system):
    assignment_name = 'assignment99'
    due_date = ''
    course = 'comp_sci'
    test_date = staff_system.create_assignment(assignment_name, due_date, course)
    assert not test_date


@pytest.fixture
def staff_system():
    staffSystem = Staff.Staff()
    return staffSystem


import pytest
import Staff


def test_assignment(staff_system):
    assignment_name = 'assignment99'
    due_date = '1/1/70'
    course = 'comp_sci'
    assert staff_system.create_assignment(assignment_name, due_date, course)


@pytest.fixture
def staff_system():
    staffSystem = Staff.Staff()
    return staffSystem


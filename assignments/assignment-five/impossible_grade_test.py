import pytest
import Staff


# Testing to see if the program will allow invalid grade values
def test_grades(staff_system):
    username = 'akend3'
    course = 'comp_sci'
    assignment = "assignment1"
    test_negative = staff_system.change_grade(username, course, assignment, -10)
    test_over = staff_system.change_grade(username, course, assignment, 101)

    if not test_negative and not test_over:
        assert True
    else:
        assert False


@pytest.fixture
def staff_system():
    staffSystem = Staff.Staff()
    return staffSystem

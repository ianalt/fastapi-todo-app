import pytest


def test_equal_or_not_equal():
    assert 3==3
    assert 3 != 1


def test_is_instance():
    assert isinstance(10, int)
    assert not isinstance(10, str)


def test_boolean():
    validated = True
    assert validated is True
    assert ("hello" == "world") is False


def test_type():
    assert type("Hello") is str
    assert type("world") is not int


def test_gt_and_lt():
    assert 4 < 10
    assert 7 > 3


def test_list():
    num_list = [1,2,3,4,5]
    any_list = [True, False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert any(any_list)


class Student:
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years


@pytest.fixture
def default_student():
    return Student("Ian", "Alt", "Computer Engineering", 5)

def test_student_initialization(default_student):
    assert default_student.first_name == "Ian", "First name should be Ian"
    assert default_student.last_name == "Alt", "Last name should be Alt"
    assert default_student.major == "Computer Engineering"
    assert default_student.years == 5
import anything
import pytest


@pytest.fixture
def data():
    return "Something"


def test_print_hello():
    """Returns the Hello World"""
    assert anything.print_hello() == "Hello world"


def test_print_given(data):
    """Returns the given data"""
    assert anything.print_given(data) == data


@pytest.mark.parametrize("number, result", [(2, 2), (13, 4), (222, 6)])
def test_sum_of_numbers(number, result):
    assert anything.sum_of_numbers(number) == result

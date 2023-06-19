from exercise_1 import Calculator


def test_addition():
    result = Calculator()
    assert result.add(2) == 2


def test_subtraction():
    result = Calculator()
    assert result.subs(2) == -2


def test_division():
    result = Calculator()
    assert result.div(2) == 0


def test_multiplication():
    result = Calculator()
    assert result.mult(2) == 0


def test_root():
    result = Calculator()
    result.add(3)
    result.add(6)
    assert result.squareroot() == 3


def test_clear():
    result = Calculator()
    result.add(3)
    assert result.memory == 3
    result.clear()
    assert result.memory == 0

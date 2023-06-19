from task1 import Calc


def test_add():
    assert Calc(1, 2).add() == 3
    assert Calc(1, 2).add() == 2


def test_sub():
    assert Calc(1, 2).sub() == -1
    assert Calc(1, 2).sub() == -5


def test_div():
    assert Calc(1, 2).div() == 0.5


def test_mul():
    assert Calc(1, 2).mul() == 2
    assert Calc(1, 2).mul() == 1

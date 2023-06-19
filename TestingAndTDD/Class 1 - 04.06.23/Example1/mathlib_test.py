import mathlib


def test_add_mul():
    """Returns correct value"""
    assert mathlib.add(2, 3) == 5
    assert mathlib.mul(2, 3) == 6


def test_type():
    """Returns correct type"""
    assert type(mathlib.add(2, 3)) == int
    assert type(mathlib.mul(2, 3)) == int

import task2a
import pytest


@pytest.mark.parametrize("string, result", [("hello", "el"),
                                            ("cupcakes", "ucks"),
                                            ("what is happening?", "hti apnn?"),
                                            (4342, "32")])
def test_odd_indexes(string, result):
    assert task2a.odd_indexes(string) == result

from task4 import get_avg, _get_data
import pytest
from unittest.mock import patch, MagicMock


def test_func():
    _get_data_mock = MagicMock(return_value="123456789")
    with patch('task4_test._get_data', _get_data_mock):
        assert get_avg(3) == 2
        assert get_avg(1) == 1
        assert get_avg(2) == 1.5


@pytest.mark.parametrize("value, result",
                         [(1, 1), (2, 1.5), (3, 2), (4, 2.5), (5, 3), (6, 3.5), (7, 4), (8, 4.5), (9, 5),
                          (999999, 5), (-5555, 5)])
def test_get_avg(value, result):
    assert get_avg(value) == result

# THIRDPARTY
from Task7 import count_nums
import pytest


@pytest.mark.parametrize("num1, num2, res", [(1, 100, 5050), (5, 10, 45), ("hello", "bye", "Impossible to count")])
def test_count_nums(num1, num2, res):
    assert count_nums(num1, num2) == res

# THIRDPARTY
from Task10 import square_sum
import pytest


# from Topic3.Task10 import UnbalancedError


@pytest.mark.parametrize("num1, num2, res", [(1, 5, 55), (5, 10, 355), ("hello", "bye", "Can't find squares")])
def test_square_sum(num1, num2, res):
    assert square_sum(num1, num2) == res


# def test_square_sum_raises_unbalanced_error():
# 	with pytest.raises(UnbalancedError):
# 		square_sum(5, 1)

# THIRDPARTY
from part3_ex2 import check_odd
import pytest


@pytest.mark.parametrize("num, res", [(4, False), (0, False), (515, True), ("hello", "It's not a number")])
def test_check_odd(num, res):
    assert check_odd(num) == res

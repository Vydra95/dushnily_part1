# THIRDPARTY
from part3_ex3 import check_even
import pytest


@pytest.mark.parametrize("num, res", [(4, True), (0, True), (515, False), ("hello", "It's not a number")])
def test_check_even(num, res):
    assert check_even(num) == res

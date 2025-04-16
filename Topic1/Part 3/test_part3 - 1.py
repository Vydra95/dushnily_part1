# THIRDPARTY
from part3_ex1 import check_positive
import pytest


@pytest.mark.parametrize("num, res", [(4, True), (0, True), (-15, False), ("hello", "It's not a number")])
def test_check_positive(num, res):
    assert check_positive(num) == res

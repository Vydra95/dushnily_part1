# THIRDPARTY
from part3_ex10 import check_odd
import pytest


@pytest.mark.parametrize(
    "num1, num2, res", [(2, 4, False), (11, 7, False), (55, 6, True), ("hello", "hi", "These aren't numbers")]
)
def test_check_odd(num1, num2, res):
    assert check_odd(num1, num2) == res

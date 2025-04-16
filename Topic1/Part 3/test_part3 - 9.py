# THIRDPARTY
from part3_ex9 import check_odd
import pytest


@pytest.mark.parametrize(
    "num1, num2, res", [(2, 4, False), (0, 356, False), (55, 6, True), ("hello", "hi", "These aren't numbers")]
)
def test_check_odd(num1, num2, res):
    assert check_odd(num1, num2) == res

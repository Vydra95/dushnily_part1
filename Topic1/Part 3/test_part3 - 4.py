# THIRDPARTY
from part3_ex4 import check_inequality
import pytest


@pytest.mark.parametrize(
    "num1, num2, res", [(4, 5, False), (0, -1, False), (515, 3, True), ("hello", "hi", "These aren't numbers")]
)
def test_check_inequality(num1, num2, res):
    assert check_inequality(num1, num2) == res

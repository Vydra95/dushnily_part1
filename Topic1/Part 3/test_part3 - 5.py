# THIRDPARTY
from part3_ex5 import check_inequality
import pytest


@pytest.mark.parametrize(
    "num1, num2, res", [(4, 5, True), (0, -1, True), (-515, 3, False), ("hello", -1, "These aren't numbers")]
)
def test_check_inequality(num1, num2, res):
    assert check_inequality(num1, num2) == res

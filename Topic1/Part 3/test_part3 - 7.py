# THIRDPARTY
from part3_ex7 import check_inequality
import pytest


@pytest.mark.parametrize(
    "num1, num2, num3, res",
    [(4, 5, 6, True), (0, -1, -2, True), (-515, -412, -1, True), ("hello", -1, 3.04, "These aren't numbers")],
)
def test_check_inequality(num1, num2, num3, res):
    assert check_inequality(num1, num2, num3) == res

# THIRDPARTY
from Task12 import factorials
import pytest


@pytest.mark.parametrize(
    "num1, num2, res",
    [(3, 5, [6, 24, 120]), (2, 6, [2, 6, 24, 120, 720]), (6, 1, []), ("hello", "bye", "Can't find factorials")],
)
def test_factorials(num1, num2, res):
    assert factorials(num1, num2) == res

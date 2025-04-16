# THIRDPARTY
from Task8 import fibonacci
import pytest


@pytest.mark.parametrize(
    "num1, num2, res",
    [
        (1, 100, [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]),
        (5, 10, [5, 8]),
        (5, 1, []),
        ("hello", "bye", "Not possible to count"),
    ],
)
def test_fibonacci(num1, num2, res):
    assert fibonacci(num1, num2) == res

# THIRDPARTY
from Task9 import prime_number
import pytest


@pytest.mark.parametrize(
    "num1, num2, res",
    [(20, 40, [23, 29, 31, 37]), (5, 10, [5, 7]), (5, 1, []), ("hello", "bye", "Can't find prime numbers")],
)
def test_prime_number(num1, num2, res):
    assert prime_number(num1, num2) == res

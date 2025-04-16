# THIRDPARTY
from part2_ex4 import find_b
import pytest


@pytest.mark.parametrize(
    "a, b, res",
    [
        (10, 3, 3),
        (9, 4, 2),
        ("a", 8, "These are not two numbers"),
    ],
)
def test_find_b(a, b, res):
    assert find_b(a, b) == res

# THIRDPARTY
from part2_ex2 import find_tons
import pytest


@pytest.mark.parametrize("n, res", [(5827.34, 5.0), (523, 0), ("Hell yeah!", "It's not a number")])
def test_find_tons(n, res):
    assert find_tons(n) == res

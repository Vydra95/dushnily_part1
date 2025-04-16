# THIRDPARTY
from part2_ex8 import find_reverse
import pytest


@pytest.mark.parametrize("num, res", [(41, 14), (52, 25), ("hello", "It's not a number")])
def test_find_reverse(num, res):
    assert find_reverse(num) == res

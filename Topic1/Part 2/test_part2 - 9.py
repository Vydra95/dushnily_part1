# THIRDPARTY
from part2_ex9 import find_hundreds
import pytest


@pytest.mark.parametrize("num, res", [(415, 4), (528, 5), ("hello", "It's not a number")])
def test_find_hundreds(num, res):
    assert find_hundreds(num) == res

# THIRDPARTY
from part2_ex1 import find_metres
import pytest


@pytest.mark.parametrize("length, res", [(421.595, 4.0), (523, 5), (82, 0), ("foo", "It's not a number")])
def test_find_metres(length, res):
    assert find_metres(length) == res

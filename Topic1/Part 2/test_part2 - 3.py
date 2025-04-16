# THIRDPARTY
from part2_ex3 import find_volume
import pytest


@pytest.mark.parametrize("a, res", [(1025, 1), (2048, 2), ("Jeez", "It's not a number")])
def test_find_volume(a, res):
    assert find_volume(a) == res

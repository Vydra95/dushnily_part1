# THIRDPARTY
from part2_ex5 import find_free_space
import pytest


@pytest.mark.parametrize("a, b, res", [(20, 6, 2), (9, 0, None)])
def test_find_free_space(a, b, res):
    assert find_free_space(a, b) == res

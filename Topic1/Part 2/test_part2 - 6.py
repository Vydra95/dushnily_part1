# THIRDPARTY
from part2_ex6 import find_figures
import pytest


@pytest.mark.parametrize("num, res", [(41, (4, 1)), (52, (5, 2)), ("hello", "It's not a number")])
def test_find_figures(num, res):
    assert find_figures(num) == res

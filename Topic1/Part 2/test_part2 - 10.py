# THIRDPARTY
from part2_ex10 import find_figures
import pytest


@pytest.mark.parametrize("num, res", [(123, (3, 2)), (52, (2, 5)), (1, (1, 0)), ("hello", "It's not a number")])
def test_find_figures(num, res):
    assert find_figures(num) == res

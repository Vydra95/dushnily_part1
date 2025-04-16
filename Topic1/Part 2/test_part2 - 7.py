# THIRDPARTY
from part2_ex7 import find_sum_product
import pytest


@pytest.mark.parametrize("num, res", [(41, (5, 4)), (52, (7, 10)), ("hello", "It's not a number")])
def test_find_sum_product(num, res):
    assert find_sum_product(num) == res

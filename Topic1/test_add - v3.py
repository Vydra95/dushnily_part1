# THIRDPARTY
from Additional_task_v3 import merge_nums
import pytest


@pytest.mark.parametrize(
    "num1, m, num2, n, res",
    [
        ([1, 14, 67, 88], 2, [84, 92, 150], 3, [1, 14, 84, 92, 150]),
        ([1, 14, 67, 88], 2, "Clare", 3, "Impossible to merge"),
    ],
)
def test_merge_nums(num1, m, num2, n, res):
    assert merge_nums(num1, m, num2, n) == res

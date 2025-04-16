# THIRDPARTY
import pytest

# FIRSTPARTY
from Additional_task import merged_nums


@pytest.mark.parametrize(
    "num1, m, num2, n, res",
    [
        ([1, 14, 67, 88], 2, [84, 92, 150], 3, [1, 14, 84, 92, 150]),
        ([1, 14, 67, 88], 2, "Clare", 3, "Impossible to merge"),
    ],
)
def test_merged_nums(num1, m, num2, n, res):
    assert merged_nums(num1, num2, m, n) == res

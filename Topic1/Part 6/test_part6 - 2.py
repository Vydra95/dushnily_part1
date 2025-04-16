# THIRDPARTY
from part6_ex2 import bubble_sort
import pytest


@pytest.mark.parametrize(
    "a, res",
    [
        ([3, 2, 1, 22, 4, 7], [1, 2, 3, 4, 7, 22]),
        ("This unit has been developed keeping in mind the ultimate comfort", "Can't sort that"),
    ],
)
def test_bubble_sort(a, res):
    assert bubble_sort(a) == res

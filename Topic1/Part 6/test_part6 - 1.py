# THIRDPARTY
from part6_ex1 import binary_search
import pytest


@pytest.mark.parametrize(
    "alist, elem, res",
    [
        ([1, 3, 5, 6, 28], 6, 3),
        ([3, 2, 1, 22, 4, 7], 6, None),
        ("This unit has been developed keeping in mind the ultimate comfort", 4, None),
    ],
)
def test_binary_search(alist, elem, res):
    assert binary_search(alist, elem) == res

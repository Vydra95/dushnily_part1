# THIRDPARTY
from part4_additional import merge_change
import pytest


@pytest.mark.parametrize(
    "my_list, your_list, res",
    [
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6, "wow"]),
        ([45, 11], [2], [45, 11, 2, "wow"]),
        (["Julie", "Francesca", "Emily"], ["Adam", "Juan"], ["Julie", "Francesca", "Emily", "Adam", "Juan", "wow"]),
        (["hello"], None, "Can't merge that"),
    ],
)
def test_merge_change(my_list, your_list, res):
    assert merge_change(my_list, your_list) == res

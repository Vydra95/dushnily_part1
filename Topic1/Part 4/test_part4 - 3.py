# THIRDPARTY
from part4_ex3 import separate_lists
import pytest


@pytest.mark.parametrize(
    "my_list, res",
    [
        (["a", "35", "2", "b", "11", "c"], (["11", "2", "35"], ["a", "b", "c"])),
        (["Stratford"], "Something's wrong"),
        ("Sandra", "Something's wrong"),
        (["Cecilia", "Abigail", "Dorothy", 464, 3, 23], "Something's wrong"),
        ([1, 466, 3, 5, 333, 211], ([1, 3, 5], [211, 333, 466])),
    ],
)
def test_separate_lists(my_list, res):
    assert separate_lists(my_list) == res

# THIRDPARTY
from part4_ex1 import hunt_list
import pytest


@pytest.mark.parametrize(
    "my_list, res",
    [
        ([1, 2, 3, 4, 5], (1, 3, [1, 2, 3])),
        ([0, 2, 5, 6, 2485, 356], (0, 5, [0, 2, 5])),
        ([5, 6], "Your list is too short"),
        ("hello", "It's not a list"),
    ],
)
def test_hunt_list(my_list, res):
    assert hunt_list(my_list) == res

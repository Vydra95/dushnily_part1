# THIRDPARTY
from part5_additional_2 import find_key
import pytest


@pytest.mark.parametrize(
    "data, b, res",
    [
        ({"name": "Bob", "age": 37, "gender": "male"}, "name", "Bob"),
        ({"name": "Bob", "age": 37, "gender": "male"}, 3, None),
        ("Debby", 1, None),
    ],
)
def test_find_key(data, b, res):
    assert find_key(data, b) == res

# THIRDPARTY
from part5_additional_3 import update_key
import pytest


@pytest.mark.parametrize(
    "data, b, n, res",
    [
        (
            {
                "name": "Bob",
                "age": 37,
                "gender": "male",
                "height": 185,
                "weight": 98,
                "occupation": "plumber",
                "car": "Toyota",
            },
            "name",
            "Rosser",
            {
                "name": ["Bob", "Rosser"],
                "age": 37,
                "gender": "male",
                "height": 185,
                "weight": 98,
                "occupation": "plumber",
                "car": "Toyota",
            },
        ),
        (
            {
                "name": "Bob",
                "age": 37,
                "gender": "male",
                "height": 185,
                "weight": 98,
                "occupation": "plumber",
                "car": "Toyota",
            },
            "bike",
            "Yamaha",
            {
                "name": "Bob",
                "age": 37,
                "gender": "male",
                "height": 185,
                "weight": 98,
                "occupation": "plumber",
                "car": "Toyota",
                "bike": [None, "Yamaha"],
            },
        ),
    ],
)
def test_update_key(data, b, n, res):
    assert update_key(data, b, n) == res

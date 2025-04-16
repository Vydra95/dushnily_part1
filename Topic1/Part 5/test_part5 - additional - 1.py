# THIRDPARTY
from part5_additional_1 import patient_update
import pytest


@pytest.mark.parametrize(
    "main_data, new_data, res",
    [
        (
            [("name", "Bob"), ("age", 37), ("gender", "male"), ("height", 185), ("weight", 98)],
            [("occupation", "plumber"), ("car", "Toyota")],
            {
                "name": "Bob",
                "age": 37,
                "gender": "male",
                "height": 185,
                "weight": 98,
                "occupation": "plumber",
                "car": "Toyota",
            },
        ),
        ([("name", "Bob"), ("age", 37)], None, "Can't update"),
    ],
)
def test_patient_update(main_data, new_data, res):
    assert patient_update(main_data, new_data) == res

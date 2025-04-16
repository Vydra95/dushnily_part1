# THIRDPARTY
from part4_ex2 import correct_name
import pytest


@pytest.mark.parametrize(
    "my_list, res",
    [
        (["Ростов", "+", "на", "-", "Дону"], "Ростов-на-Дону"),
        (["Stratford", "?", "upon", "-", "Avon"], "Stratford-upon-Avon"),
        (["Cheshire"], "Something's wrong"),
        ("hello", "Can't change that"),
    ],
)
def test_correct_name(my_list, res):
    assert correct_name(my_list) == res

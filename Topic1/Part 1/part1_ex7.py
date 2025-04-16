# STDLIB
from typing import Any


Pi = 3.14


def get_circle_data(r: int | float) -> tuple[float, float | Any]:
    length = 2 * Pi
    s = Pi * r**2
    return (length, s)


print(get_circle_data(r=3))

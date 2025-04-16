"""Факториалы в заданном диапазоне"""

# STDLIB
from math import factorial


# from typing import List


a = "hello"
b = "bye"


def factorials(a: int, b: int) -> list[int] | str:
    list_list = []
    try:
        for i in range(a, b + 1):
            list_list.append(factorial(i))
        return list_list
    except TypeError:
        return "Can't find factorials"


print(factorials(a, b))

"""Факториалы в заданном диапазоне"""

# STDLIB
from math import factorial
from typing import List


a = 3
b = 5


def factorials(a: int, b: int) -> List[int]:
    list_list = []
    for i in range(a, b + 1):
        list_list.append(factorial(i))

    return list_list


print(factorials(a, b))

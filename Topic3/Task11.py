"""Вывести значения функции y=x^2 от 1 до 10 с шагом 0.5"""

# STDLIB
from typing import List


def func() -> List[int]:
    step = 0.5
    llist = []
    x = 1
    while x <= 10:
        y = x**2
        llist.append(y)
        x += step
    return llist


print(func())

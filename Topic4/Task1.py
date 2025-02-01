"""Даны три целых числа. Найти количество положительных чисел"""


def find_positive() -> int:
    a = 5
    b = -7
    c = 1
    counter = 0
    if a > 0:
        counter += 1
    if b > 0:
        counter += 1
    if c > 0:
        counter += 1
    return counter


print(find_positive())

"""Сумма квадратов в заданном диапазоне"""

a = 5
b = 35


def square_sum(a: int, b: int) -> int:
    n = 0
    for i in range(a, b + 1):
        n += i**2
    return n


print(square_sum(a, b))

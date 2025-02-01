"""Даны три числа, найти наименьшее"""


def min_of_three() -> int:
    a = 3
    b = 1
    c = 15
    x = a
    y = c
    minimal = 0
    if a > b:
        x = b
    if b > c:
        y = c
    if x > y:
        minimal = y
    if y > x:
        minimal = x
    return minimal


print(min_of_three())

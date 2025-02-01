"""Даны два числа. Вывести сначала большее из них, а потом меньшее"""


def comparison() -> tuple:
    a = 5
    b = 7
    if b > a:
        a, b = b, a
    return a, b


print(comparison())

"""Даны два числа. Вывести большее из них"""


def the_biggest() -> int:
    a = 5
    b = 7
    biggest = 0
    if a > b:
        biggest = a
    else:
        biggest = b
    return biggest


print(the_biggest())

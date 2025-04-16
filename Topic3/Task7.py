"""Найти сумму всех чисел от 1 до 100."""


def count_nums(a, b):
    n = 0
    try:
        for i in range(a, b + 1):
            n += i
        return n
    except TypeError:
        return "Impossible to count"


print(count_nums(5, 10))

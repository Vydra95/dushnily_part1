"""Сумма квадратов в заданном диапазоне"""

a = 5
b = 1


class UnbalancedError(Exception):
    def __init__(self, message):
        super().__init__(message)


def square_sum(a: int, b: int) -> int | str:
    n = 0
    try:
        if isinstance(a, int) and isinstance(b, int) and a > b:
            raise UnbalancedError("Can't find squares")
        for i in range(a, b + 1):
            n += i**2
        return n
    except TypeError:
        return "Can't find squares"
    except UnbalancedError:
        raise

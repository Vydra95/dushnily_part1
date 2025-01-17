# STDLIB
import math


def main(a: int, b: int) -> float:
    factorial = math.factorial(a)
    try:
        division = factorial / b
    except ZeroDivisionError:
        return 0
    else:
        division = factorial / b
        return division


print(main(50, 0))

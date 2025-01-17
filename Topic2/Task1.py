# STDLIB
import logging
from math import sqrt


logging.basicConfig(level=logging.INFO, filename="py_log_1.log", filemode="a")

a, b, c = int(input()), int(input()), int(input())


class NegativeValueError(Exception):
    pass


try:
    d = b**2 - (4 * a * c)
    if d > 0:
        result = ((-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a))
        print(result)
        logging.info(f"The answer is {result}")
    elif d == 0:
        result = -b / (2 * a)
        print(result)
        logging.info(f"The answer is {result}")
    elif d < 0:
        raise NegativeValueError
except NegativeValueError:
    logging.error("NegativeValueError", exc_info=True)
    print("Try again with different coefficients")

# STDLIB
import logging
import random


logging.basicConfig(level=logging.INFO, filename="py_log_2.log", filemode="a")


class NegativeValueError(Exception):
    pass


class ExcessiveValueError(Exception):
    pass


print("Введи два числа, больше 0 и меньше 1000")
a, b = int(input()), int(input())

try:
    if a > 0 and b < 1000:
        number = random.randint(a, b)
        print(number)
        logging.info(f"Получилось {number}")
    elif a < 0 or b < 0:
        raise NegativeValueError
    elif a >= 1000 or b >= 1000:
        raise ExcessiveValueError
except NegativeValueError:
    print("Числа должны быть от 0 до 1000! Попробуй ещё раз")
    logging.error("NegativeValueError", exc_info=True)
except ExcessiveValueError:
    print("Числа должны быть от 0 до 1000! Попробуй ещё раз")
    logging.error("ExcessiveValueError", exc_info=True)

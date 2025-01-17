# STDLIB
import logging


logging.basicConfig(level=logging.INFO, filename="py_log_3.log", filemode="a")

print("Введите три числа")
a, b, c = input(), input(), input()

try:
    a, b, c = int(a), int(b), int(c)
    alist = [a, b, c]
    mean_value = sum(alist) / len(alist)
    print(mean_value)
    logging.info(f"Получилось {mean_value}")
except ValueError:
    print("Могу вычислить только для чисел")
    logging.error("TypeError", exc_info=True)

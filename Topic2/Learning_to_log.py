# STDLIB
import logging


logging.basicConfig(level=logging.WARNING, filename="py_log.log", filemode="w")

x_vals = [2, 3, 6, 4, 10]
y_vals = [5, 7, 12, 0, 1]

for x_val, y_val in zip(x_vals, y_vals):
    x, y = x_val, y_val
    logging.warning(f"The values of x and y are {x} and {y}.")
    try:
        z = x / y
        logging.warning(f"x/y successful with result: {z}.")
    except ZeroDivisionError:
        logging.exception("ZeroDivisionError")

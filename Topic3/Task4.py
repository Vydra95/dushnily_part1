"""Одна функция создает список с числами от 0 до 1000 с фагом 1 через цикл for,
вторая делает то же самое, но через цикл while"""

# STDLIB
import time
from typing import List


def for_cycle() -> List[int]:
    alist = []
    for i in range(0, 1001, 1):
        alist.append(i)
    return alist


print(for_cycle())

start_time = time.perf_counter_ns()
result = for_cycle()
end_time = time.perf_counter_ns()

execution_time = end_time - start_time
print(f"Время выполнения: {execution_time}")


def while_cycle() -> List[int]:
    alist = []
    i = 0
    while i <= 1000:
        alist.append(i)
        i += 1
    return alist


print(while_cycle())

start_time = time.perf_counter_ns()
result = while_cycle()
end_time = time.perf_counter_ns()

execution_time = end_time - start_time
print(f"Время выполнения: {execution_time}")

numbers = [x for x in range(1001)]
print(numbers)

start_time = time.perf_counter_ns()
result = numbers
end_time = time.perf_counter_ns()

execution_time = end_time - start_time
print(f"Время выполнения: {execution_time}")

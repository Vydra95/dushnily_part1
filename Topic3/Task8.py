"""Числа Фибоначчи"""

# STDLIB
from typing import List


a = 0
b = 1
start_point = 100
end_point = 1000


def fibonacci(a: int, b: int, start_point: int, end_point: int) -> List[int]:
    my_list = []
    for i in range(a, end_point):
        n = a + b
        my_list.append(n)
        a = b
        b = n
    my_list = [j for j in my_list if j >= start_point and j <= end_point]
    return my_list


print(fibonacci(a, b, start_point, end_point))

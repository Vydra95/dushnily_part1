"""Числа Фибоначчи"""

# STDLIB
from typing import List


start_point = 5
end_point = 1


def fibonacci(start_point: int, end_point: int) -> List[int] | str:
    my_list = []
    a = 0
    b = 1
    try:
        for i in range(a, end_point):
            n = a + b
            my_list.append(n)
            a = b
            b = n
        my_list = [j for j in my_list if j >= start_point and j <= end_point]
        return my_list
    except TypeError:
        return "Not possible to count"


print(fibonacci(start_point, end_point))

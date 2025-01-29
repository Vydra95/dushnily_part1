"""Все простые числа диапазона"""

# STDLIB
from typing import List


a = 20
b = 80


def prime_number(a: int, b: int) -> List[int]:
    n = b
    primes = [i for i in range(n + 1)]
    primes[1] = 0
    i = 2
    while i <= n:
        if primes[i] != 0:
            j = i + i
            while j <= n:
                primes[j] = 0
                j = j + i
        i += 1
    primes = [i for i in primes if i != 0 and i >= a]
    return primes


print(prime_number(a, b))

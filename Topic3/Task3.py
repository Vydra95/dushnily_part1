"""Задача про таблицу умножения от 0 до 9"""

for i in range(0, 10):
    for j in range(0, 10):
        print(f"{i} x {j} = {i * j}", end="   ")
    print()

""" Задача про чётные числа из заданного диапазона"""

try:
    alist = []
    for i in range(1, 100):
        if i % 2 == 0:
            alist.append(i)
    print(alist)
except NameError:
    print("Только числа!")

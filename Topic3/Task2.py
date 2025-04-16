""" Задача про чётные числа из заданного диапазона"""


def find_evens(a, b):
    try:
        alist = []
        for i in range(a, b):
            if i % 2 == 0:
                alist.append(i)
        return alist
    except TypeError:
        return "Только числа!"


print(find_evens(1, 5))

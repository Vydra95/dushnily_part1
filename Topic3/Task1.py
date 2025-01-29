""" Задача про среднее арифметическое списка или кортежа"""


class EmptyList(Exception):
    pass


try:
    n = [1, 2, 3]
    s = 0
    if len(n) == 0:
        raise EmptyList
    if len(n) > 0:
        for i in n:
            s += i
            mean = s / len(n)
        print("Среднее арифметическое:", mean)
except EmptyList:
    print("Нет элементов в списке")
    raise SystemExit
except NameError:
    print("Только числа")

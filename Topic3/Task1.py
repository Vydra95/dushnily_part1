""" Задача про среднее арифметическое списка или кортежа"""


class EmptyList(Exception):
    pass


n = [1, 2, 3]


def mean_list(n: list):
    try:
        s = 0
        if len(n) == 0:
            raise EmptyList
        if len(n) > 0:
            for i in n:
                s += i
                mean = s / len(n)
            return f"Среднее арифметическое: {mean}"
    except EmptyList:
        print("Нет элементов в списке")
        raise SystemExit
    except NameError:
        return "Только числа"


print(mean_list(n))

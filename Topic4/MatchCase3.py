"""Следующая дата"""

d = 1
m = 2
a = [x for x in range(1, 30)]
b = [x for x in range(1, 29)]
c = [x for x in range(1, 27)]
x = "Что-то не то"


def next_date(d: int, m: int) -> list:
    match m:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            match d:
                case _ if d in a:
                    d += 1
                case 31:
                    d = 1
                    m += 1
                case _:
                    d = x
                    m = None
        case 4 | 6 | 9 | 11:
            match d:
                case _ if d in b:
                    d += 1
                case 30:
                    d = 1
                    m += 1
                case _:
                    d = x
                    m = None
        case 2:
            match d:
                case _ if d in c:
                    d += 1
                case 28:
                    d = 1
                    m += 1
                case _:
                    d = x
                    m = None
        case _:
            m = x
            d = None

    return [d, m]


print(next_date(d, m))

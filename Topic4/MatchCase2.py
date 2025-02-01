"""Число дней в месяце"""

month = 5


def months_days() -> None:
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            print(31)
        case 4 | 6 | 9 | 11:
            print(30)
        case 2:
            print(28)
        case _:
            print("На Земле только 12 месяцев")
    return None


months_days()

"""Оценка"""

k = 31


def check_your_mark(k: int) -> None:
    match k:
        case 1:
            print("Плохо")
        case 2:
            print("Неудовлетворительно")
        case 3:
            print("Удовлетворительно")
        case 4:
            print("Хорошо")
        case 5:
            print("Отлично")
        case _:
            print("Это не оценка")
    return None


check_your_mark(k)

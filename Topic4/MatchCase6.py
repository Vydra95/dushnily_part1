"""Калькулятор"""


def calculator() -> int | None:
    a = 200
    b = 1
    c = "/"
    d = 0
    match (a, b):
        case int(), int():
            pass
        case int(), float():
            pass
        case float(), int():
            pass
        case float(), float():
            pass
        case _:
            print("Считаю только цифры")
            return
    match c:
        case "+":
            d = a + b
        case "-":
            d = a - b
        case "*":
            d = a * b
        case "/" | ":":
            match b:
                case 0:
                    print("На ноль делить нельзя!")
                    return
            d = a / b
        case _:
            d = None
            print("Некорректный знак")
    return d


print(calculator() if calculator() is not None else "")

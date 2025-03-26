"""
Создайте класс функтуру `Calculator`, который умеет складывать, вычитать, делить и умножать два числа
"""


class Calculator:

    def __init__(self):
        self.x = 0
        self.y = 0

    def __call__(self, operator, x, y, *args, **kwargs):
        self.x = x
        self.y = y
        return {
            "add": lambda: x + y,
            "sub": lambda: x - y,
            "mul": lambda: x * y,
            "div": lambda: x / y,
        }.get(operator, lambda: "Can't process")()


c = Calculator()
print(c("pow", 5, 7))

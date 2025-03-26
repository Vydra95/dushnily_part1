"""
Calculator и перезагрузка его метода в наследуемом классе
"""


class Calculator:
    def adding(self, a, b):
        result = None
        try:
            result = a + b
        except TypeError:
            print("Могу сложить только числа")
        return result


class Fuser(Calculator):
    def adding(self, a, b):
        if not isinstance(a, str) or not isinstance(b, str):
            result = None
            print("Могу соединить только строки")
        else:
            result = a + b
        return result


attempt1 = Calculator()
print(attempt1.adding(3, 4))
attempt2 = Fuser()
print(attempt2.adding("hell", "o"))

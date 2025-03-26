"""
Все возможные магические методы
"""

# STDLIB
from math import ceil
import sys


class AllMethods:  # Предположим, что этот класс нужен для работы со статистическими данными
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.id = a * b
        self.box = [hash(self.a), hash(self.b), hash(self.id)]

    def __call__(self, *args, **kwargs):
        obj = self.__new__(self, *args, **kwargs)
        self.__init__(obj, *args, *kwargs)
        print("Был вызван метод __call__")
        return obj

    def __hash__(self):
        print("Был вызван метод __hash__")
        return hash(self.id)

    def __str__(self):
        print("Был вызван метод __str__")
        return f"{self.id}"

    def __repr__(self):
        print("Был вызван метод __repr__")
        return f"{self.__class__}: {self.id}"

    def __len__(self):
        if self.a > 0 and self.b > 0:
            alist = [self.a, self.b]
        elif self.b < 0 < self.a:
            alist = [self.a]
        elif self.a < 0 < self.b:
            alist = [self.b]
        else:
            alist = []
        print("Был вызван метод __len__")
        return len(alist)

    def __abs__(self):
        print("Был вызван метод __abs__")
        return [abs(self.a), abs(self.b)]

    def __add__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно сложить только int или AllMethods")
        print("Был вызван метод __add__")
        return self.id + other

    def __iadd__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно сложить только int или AllMethods")
        print("Был вызван метод __iadd__")
        return self.id + other

    def __radd__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно сложить только int или AllMethods")
        print("Был вызван метод __radd__")
        return self.id + other

    def __sub__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно вычесть только int или AllMethods")
        print("Был вызван метод __sub__")
        return self.id - other

    def __isub__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно вычесть только int или AllMethods")
        print("Был вызван метод __isub__")
        return self.id - other

    def __rsub__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно вычесть только int или AllMethods")
        print("Был вызван метод __rsub__")
        return self.id - other

    def __mul__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно умножить только int или AllMethods")
        print("Был вызван метод __mul__")
        return self.id * other

    def __imul__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно умножить только int или AllMethods")
        print("Был вызван метод __imul__")
        return self.id * other

    def __rmul__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно умножить только int или AllMethods")
        print("Был вызван метод __rmul__")
        return self.id * other

    def __truediv__(self, other):
        if type(other) is not int and type(other) is not float:
            if type(other) is not AllMethods:
                raise ArithmeticError("Можно поделить только int или AllMethods")
            elif type(other) is AllMethods:
                return self.id / other.id
        else:
            return self.id / other
        print("Был вызван метод __truediv__")

    def __itruediv__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно поделить только int или AllMethods")
        print("Был вызван метод __itruediv__")
        return self.id / other

    def __floordiv__(self, other):
        if type(other) is not int and type(other) is not float:
            if type(other) is not AllMethods:
                raise ArithmeticError("Можно поделить только int или AllMethods")
            elif type(other) is AllMethods:
                return self.id // other.id
        else:
            return self.id // other
        print("Был вызван метод __floordiv__")

    def __ifloordiv__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно поделить только int или AllMethods")
        print("Был вызван метод __ifloordiv__")
        return self.id // other

    def __mod__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно поделить только int или AllMethods")
        print("Был вызван метод __mod__")
        return self.id % other

    def __imod__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно поделить только int или AllMethods")
        print("Был вызван метод __imod__")
        return self.id % other

    def __rmod__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно поделить только int или AllMethods")
        print("Был вызван метод __rmod__")
        return self.id % other

    def __pow__(self, power, modulo=None):
        print("Был вызван метод __pow__")
        return self.id**power

    def __rpow__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно возвести в степень только int или AllMethods")
        print("Был вызван метод __rpow__")
        return other**self.id

    def __ipow__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно возвести в степень только int или AllMethods")
        print("Был вызван метод __ipow__")
        return self.id**other.id

    def __eq__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно сравнить только с int или AllMethods")
        print("Был вызван метод __eq__")
        return self.id == other.id

    def __ne__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно сравнить только с int или AllMethods")
        print("Был вызван метод __ne__")
        return self.id != other.id

    def __lt__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно сравнить только с int или AllMethods")
        print("Был вызван метод __lt__")
        return self.id < other.id

    def __le__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно сравнить только с int или AllMethods")
        print("Был вызван метод __le__")
        return self.id <= other.id

    def __gt__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно сравнить только с int или AllMethods")
        print("Был вызван метод __gt__")
        return self.id > other.id

    def __ge__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, AllMethods)):
            raise ArithmeticError("Можно сравнить только с int или AllMethods")
        print("Был вызван метод __ge__")
        return self.id >= other.id

    def __round__(self, n=2):
        print("Был вызван метод __round__")
        return [round(self.a, n), round(self.b, n)]

    def __ceil__(self):
        print("Был вызван метод __ceil__")
        return [ceil(self.a), ceil(self.b)]

    def __bool__(self):
        print("Был вызван метод __bool__")
        return self.a == self.b

    def __getitem__(self, item):
        if 0 <= item < len(self.box):
            return self.box[item]
        else:
            raise IndexError("Неверный индекс")
        print("Был вызван метод _getitem__")

    def __setitem__(self, key, value):
        if key >= len(self.box):
            raise IndexError("Неверный индекс")
        else:
            self.box[key] = hash(value)
        print("Был вызван метод __setitem__")

    def __delitem__(self, key):
        del self.box[key]
        print("Был вызван метод __delitem__")

    def __dir__(self):
        print("Был вызван метод __dir__")
        return [f"a = {self.a}, b = {self.b}, id = {self.id}, box = {self.box}"]

    def __sizeof__(self):
        size = object.__sizeof__(self)
        size += sum(sys.getsizeof(value) for value in self.__dict__.values())
        print("Был вызван метод __sizeof__")
        return size


stat = AllMethods(2.054857, 4.386475636)
stat2 = AllMethods(3, 7)
test = 2 % stat2
print(test)

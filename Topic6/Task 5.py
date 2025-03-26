"""
Обращение к приватным и защищённым атрибутам
"""


class Car:
    def __init__(self, wheels=4, number=""):
        self._wheels = wheels
        self.__number = number


honda = Car(4, "М143АЕ")
print(honda._wheels)  # на экран выводится значение
print(honda.__number)  # атрибут не найден

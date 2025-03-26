"""
Наследование классов Car и Moped от класса MeansOfTransport
"""


class MeansOfTransport:
    def __init__(self, colour, brand):
        self.__colour = colour
        self.__brand = brand


class Car(MeansOfTransport):
    def __init__(self, wheels, colour, brand):
        super().__init__(colour, brand)
        self.wheels = wheels


class Moped(MeansOfTransport):
    def __init__(self, wheels, colour, brand):
        super().__init__(colour, brand)
        self.wheels = wheels


Car(4, "grey", "Honda")
Moped(2, "red", "Yamaha")

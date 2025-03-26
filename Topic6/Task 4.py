"""
Статичееский метод подсчёта времени поездки
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

    @staticmethod
    def ride_time(distance, max_speed) -> str:
        time = distance // max_speed
        return f"{time} h"


Car(4, "grey", "Honda")
Moped(2, "red", "Yamaha")
print(Moped.ride_time(100, 100))

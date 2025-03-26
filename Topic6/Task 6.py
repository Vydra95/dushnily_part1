"""
Метод класса car_drive
"""


class MeansOfTransport:
    def __init__(self, colour, brand):
        self.__colour = colour
        self.__brand = brand


class Car(MeansOfTransport):
    def __init__(self, wheels, colour, brand, car_drive=4):
        super().__init__(colour, brand)
        self.wheels = wheels
        self.car_drive = car_drive

    @classmethod
    def show_drive(cls):
        cls.car_drive = 4
        print(cls.car_drive)


celica = Car(4, "yellow", "toyota")
celica.show_drive()

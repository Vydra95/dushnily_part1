"""
Сеттеры и геттеры для цвета и марки
"""


class MeansOfTransport:
    def __init__(self, colour, brand):
        self.__colour = colour
        self.__brand = brand

    def set_colour(self, colour):
        if colour in ("yellow", "red", "blue"):
            self.__colour = colour
        else:
            print("Беспонтовый цвет")

    def get_colour(self):
        return self.__colour

    def set_brand(self, brand):
        if brand in ("Toyota", "BMW", "Volkswagen", "Porsche", "Audi"):
            self.__brand = brand
        else:
            print("Беспонтовая марка")

    def get_brand(self):
        return self.__brand


car = MeansOfTransport("red", "Toyota")
car.set_brand("Lada")

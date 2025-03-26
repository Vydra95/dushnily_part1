"""
Методы для получения цвета и марки
"""


class MeansOfTransport:
    colour = "yellow"
    brand = "Toyota"

    @classmethod
    def show_colours(cls):
        print(cls.colour)

    @classmethod
    def show_brand(cls):
        print(cls.brand)


car = MeansOfTransport
car.show_brand()

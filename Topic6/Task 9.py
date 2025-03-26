"""
Абстрактный класс `Animals`, класс Cat, который наследуется от класса Animals, в нём метод voice
"""

# STDLIB
import abc


class Animals(abc.ABC):
    def voice(self):
        pass


class Cat(Animals):
    def voice(self):
        return "meow"


Siamese = Cat()
print(Siamese.voice())

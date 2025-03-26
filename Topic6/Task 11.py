"""
Изменяемый Singleton
"""


class Dog:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Dog.__instance = None

    def __init__(self, name):
        self.name = name

    def voice(self):
        if "a" in self.name:
            print("grrrr")
        elif "e" in self.name:
            print("awoooooo")
        elif "o" in self.name:
            print("woof")
        elif "i" in self.name:
            print("bow wow")
        elif "u" in self.name:
            print("arf arf")

    def good_boy(self):
        print(f"Good boy, {self.name}!")


Husky = Dog("Fluffy")
Chihuahua = Dog("Adam")
Chihuahua = Dog("Lincoln")

Chihuahua.voice()
Chihuahua.good_boy()

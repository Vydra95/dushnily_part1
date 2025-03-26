"""
Сделайте класс `GenerateFibonachi`, который генерирует числа Фибоначчи
"""


class GenerateFibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def generate(self, end_point):
        try:
            my_list = []
            for i in range(self.a, end_point):
                n = self.a + self.b
                my_list.append(n)
                self.a = self.b
                self.b = n
            my_list = [j for j in my_list if j <= end_point]
            return my_list
        except TypeError:
            print("End point must be a number")
            return ""


attempt1 = GenerateFibonacci()
print(attempt1.generate("100"))

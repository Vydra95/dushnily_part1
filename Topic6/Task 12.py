"""
Напишите класс, который принимает список людей и итерируется
"""


class People:
    def __init__(self, alist):
        self.alist = alist

    def add_new_people(self, name):
        self.alist.append(name)

    def __next__(self):
        if self.i < len(self.alist):
            res = self.alist[self.i]
            self.i += 1
            return res
        else:
            raise StopIteration

    def __iter__(self):
        self.i = 0
        return self


count = People(["Sandra", "Mary", "Evelyn"])
count.add_new_people("Debra")
count.add_new_people("Lily")

for x in count:
    print(x)

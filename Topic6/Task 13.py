"""
3 любые атрибута и при изменении логгировать (выводить) всё в консоль (при изменении
выводит сообщение в формате "старое -> новое")
"""


class Descriptor:
    def __set_name__(self, instance, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        old_value = instance.__dict__.get(self.name, None)
        instance.__dict__[self.name] = value
        print(old_value, "->", instance.__dict__[self.name])
        setattr(instance, self.name, value)


class Coordinates:
    x = Descriptor()
    y = Descriptor()
    z = Descriptor()


coord_set1 = Coordinates()
coord_set1.x = 10
coord_set1.y = 12
coord_set1.z = 5
coord_set1.x = 40

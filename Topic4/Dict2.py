"""Где техника?"""

vehicle = "Грузовик ЗИЛ-20"


def our_machines(vehicle: str) -> str:
    return {
        "Грузовик ЗИЛ-20": lambda: "x = 250.5, y = -150",
        "Машина x-5": lambda: "x = 111.1, y = 50",
        "Вертолет АМ-13": lambda: "x = -303.5, y = -1300",
        "Подводная лодка А-16": lambda: "x = -1000, y = -20000",
    }.get(vehicle, lambda: "Такого нет, а почему вы спрашиваете?")()


print(our_machines(vehicle))

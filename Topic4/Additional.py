"""Где техника на карте?"""

vehicle = "Грузовик ЗИЛ-20"


def our_machines(vehicle: str) -> dict:
    return {
        "Грузовик ЗИЛ-20": lambda: {"x": 250.5, "y": -150},
        "Машина x-5": lambda: {"x": 111.1, "y": 50},
        "Вертолет АМ-13": lambda: {"x": -303.5, "y": -1300},
        "Подводная лодка А-16": lambda: {"x": -1000, "y": -20000},
    }.get(vehicle, lambda: "Такого нет, а почему вы спрашиваете?")()


coordinates = our_machines(vehicle)

if coordinates["x"] > 0 and coordinates["y"] > 0:
    print("На северо-востоке")
elif coordinates["x"] < 0 < coordinates["y"]:
    print("На северо-западе")
elif coordinates["x"] < 0 and coordinates["y"] < 0:
    print("На юго-западе")
elif coordinates["y"] < 0 < coordinates["x"]:
    print("На юго-востоке")

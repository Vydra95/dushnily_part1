""""Цвета в словаре"""

a = "yellow"


def colours(a: str) -> str:
    return {
        "red": lambda: "красный",
        "yellow": lambda: "жёлтый",
        "green": lambda: "зелёный",
        "blue": lambda: "синий",
        "purple": lambda: "сиреневый",
        "pink": lambda: "розовый",
        "black": lambda: "чёрный",
        "white": lambda: "белый",
        "grey": lambda: "серый",
        "orange": lambda: "оранжевый",
    }.get(a, lambda: "Не знаю такой цвет")()


print(colours(a))

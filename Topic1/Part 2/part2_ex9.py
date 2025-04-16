def find_hundreds(a: int):
    try:
        hundred = a // 100
        return hundred
    except (TypeError, ValueError):
        return "It's not a number"


print(find_hundreds(624))

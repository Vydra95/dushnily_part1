def find_tons(m: int | float) -> int | str:
    try:
        tons = m // 1000
        return tons
    except (TypeError, ValueError):
        return "It's not a number"


print(find_tons(m=5827.34))

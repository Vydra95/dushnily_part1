def find_metres(length: int | float) -> int | float | str:
    try:
        metres = length // 100
        return metres
    except (TypeError, ValueError):
        return "It's not a number"


print(find_metres(length=421.595))

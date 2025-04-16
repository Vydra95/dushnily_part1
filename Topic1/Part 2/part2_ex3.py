def find_volume(a: int):
    try:
        volume = a // 1024
        return volume
    except (TypeError, ValueError):
        return "It's not a number"


print(find_volume(a=1025))

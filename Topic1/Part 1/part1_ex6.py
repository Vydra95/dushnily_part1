def get_parallelepiped(a, b, c: int | float) -> float:
    v = a * b * c
    s = 2 * (a * b + b * c + a * c)
    return v, s


print(get_parallelepiped(a=2, b=3, c=1))

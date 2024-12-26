def get_cube(a: int | float) -> float:
    v = a ** 3
    s = 6 * a ** 2
    return v, s

print(get_cube(a = 3))
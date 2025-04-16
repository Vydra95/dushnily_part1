def get_data(a, b: float) -> tuple[float, float]:
    s = a * b
    p = 2 * (a + b)
    return s, p


print(get_data(2, 5))

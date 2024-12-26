Pi = 3.14
def get_circle_data(r: int | float) -> float:
    l = 2 * Pi
    s = Pi * r**2
    return l, s

print(get_circle_data(r = 3))
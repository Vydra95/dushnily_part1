def get_data(a, b: int | float) -> float:
    sum = a**2 + b**2
    difference = a**2 - b**2
    multiplication = a**2 * b**2
    distraction = a**2 / b**2
    return sum, difference, multiplication, distraction


print(get_data(a=2, b=3))

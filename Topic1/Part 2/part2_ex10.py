def find_figures(a: int):
    try:
        a3 = a % 10
        a2 = (a // 10) % 10
        return a3, a2
    except (TypeError, ValueError):
        return "It's not a number"


print(find_figures(7))

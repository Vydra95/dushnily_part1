def find_figures(a: int):
    try:
        left = a // 10
        right = a % 10
        return left, right
    except (TypeError, ValueError):
        return "It's not a number"


print(find_figures(25))

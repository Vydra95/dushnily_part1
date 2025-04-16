def check_positive(a: int):
    try:
        yes = a >= 0
        return yes
    except (TypeError, ValueError):
        return "It's not a number"


print(check_positive(0))

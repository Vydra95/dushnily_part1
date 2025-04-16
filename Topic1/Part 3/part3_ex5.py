def check_inequality(a, b: int):
    try:
        yes = a >= 0 or b < -2
        return yes
    except (TypeError, ValueError):
        return "These aren't numbers"


print(check_inequality(5, 3))

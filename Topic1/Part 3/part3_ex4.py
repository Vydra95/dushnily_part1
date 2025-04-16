def check_inequality(a, b: int):
    try:
        yes = a > 2 and b <= 3
        return yes
    except (TypeError, ValueError):
        return "These aren't numbers"


print(check_inequality(5, 3))

def check_odd(a, b: int):
    try:
        yes = a % 2 != 0 or b % 2 != 0
        return yes
    except (TypeError, ValueError):
        return "These aren't numbers"


print(check_odd(7, 4))

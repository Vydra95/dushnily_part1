def check_inequality(a, b, c: int):
    try:
        yes = a < b < c or a > b > c
        return yes
    except (TypeError, ValueError):
        return "These aren't numbers"


print(check_inequality(5, 3, 2))

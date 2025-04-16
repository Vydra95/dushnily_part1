def check_even(a: int):
    try:
        yes = a % 2 == 0
        return yes
    except (TypeError, ValueError):
        return "It's not a number"


print(check_even(10))

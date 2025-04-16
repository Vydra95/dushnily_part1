def find_b(a, b: int):
    try:
        amount_b = a // b
        return amount_b
    except (TypeError, ValueError):
        return "These are not two numbers"


print(find_b(10, 3))

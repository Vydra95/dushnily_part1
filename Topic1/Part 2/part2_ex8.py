def find_reverse(a: int):
    try:
        a1 = a // 10
        a2 = a % 10
        reverse = a2 * 10 + a1
        return reverse
    except (TypeError, ValueError):
        return "It's not a number"


print(find_reverse(72))

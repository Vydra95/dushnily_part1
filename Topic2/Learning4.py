a, b = input(), input()


def sums(a: int, b: int) -> str:
    try:
        a = int(a)
        b = int(b)
        c = a + b
        return f"{c}"
    except ValueError:
        return "try it with numbers!"


print(sums(a, b))

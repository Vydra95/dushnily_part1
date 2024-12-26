def find_figures(a: int):
    a3 = a % 10
    a2 = (a // 10) % 10
    return a3, a2

print(find_figures(728))


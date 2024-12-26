def find_figures(a: int):
    left = a // 10
    right = a % 10
    return left, right

print(find_figures(25))
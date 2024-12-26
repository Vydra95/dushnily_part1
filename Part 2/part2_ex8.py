def find_reverse(a: int):
    a1 = a // 10
    a2 = a % 10
    reverse = a2 * 10 + a1
    return reverse

print(find_reverse(72))
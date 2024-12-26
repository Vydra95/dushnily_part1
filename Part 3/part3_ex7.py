def check_inequality(a, b, c: int):
    yes = a < b < c or a > b > c
    return yes
print(check_inequality(5,3, 2))
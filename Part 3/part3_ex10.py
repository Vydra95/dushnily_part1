def check_odd(a, b: int):
    yes = (a % 2 != 0 and b % 2 == 0) or (b % 2 != 0 and a % 2 == 0)
    return yes
print(check_odd(11, 13))
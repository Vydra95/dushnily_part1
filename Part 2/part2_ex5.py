def find_free_space(a, b: (int, int)):
    free_space = a - (b * (a // b))
    return free_space

print(find_free_space(20, 6))
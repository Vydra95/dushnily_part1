def find_free_space(a, b: (int, int)):
    try:
        free_space = a - (b * (a // b))
        return free_space
    except Exception:
        return


print(find_free_space(20, 6))

num1 = [1, 14, 67, 88]
m = 2
num2 = [84, 92, 150]
n = 3


def merged_nums(num1, num2, m, n):
    try:
        a, b = num1[0:m], num2[0:n]
        a.extend(b)
        a.sort()
        return a
    except TypeError:
        return "Impossible to merge"


print(merged_nums(num1, num2, m, n))

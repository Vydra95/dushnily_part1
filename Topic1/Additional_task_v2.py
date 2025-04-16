num1 = [1, 2, 3, 0, 0, 0]
m = 3
num2 = [2, 5, 6]
n = 3


def merged_nums(num1, num2, m, n):
    try:
        total = [x for x in num1 if num1.index(x) < m] + [x for x in num2 if num2.index(x) < n]
        for i in range(m + n - 1):
            for j in range(m + n - 1 - i):
                if total[j] > total[j + 1]:
                    total[j], total[j + 1] = total[j + 1], total[j]
        return total
    except TypeError:
        return "Impossible to merge"


print(merged_nums(num1, num2, m, n))

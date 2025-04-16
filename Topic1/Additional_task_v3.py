num1 = [2, 3, 5, 11]
m = 2
num2 = [2, 3, 6]
n = 2


def merge_nums(num1, m, num2, n):
    total = []
    a = 0
    b = 0
    try:
        while len(total) < m + n:
            if a == m:
                total += [num2[b]]
                b += 1
            elif b == n:
                total += [num1[a]]
                a += 1
            elif num1[a] < num2[b]:
                total += [num1[a]]
                a = a + 1
            elif num1[a] > num2[b]:
                total += [num2[b]]
                b = b + 1
            elif num1[a] == num2[b]:
                total += [num1[a], num2[b]]
                a = a + 1
                b = b + 1
        return total
    except TypeError:
        return "Impossible to merge"


print(merge_nums(num1, m, num2, n))

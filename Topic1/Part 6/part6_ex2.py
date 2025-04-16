a = [1, 2, 7, 13, 25, 6, 9, 20, 4]


def bubble_sort(a):
    try:
        for i in range(len(a) - 1):
            for j in range(len(a) - 1 - i):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a
    except TypeError:
        return "Can't sort that"


print(bubble_sort(a))

alist = [1, 2, 7, 13, 25, 6, 9, 20, 4]

def binary_search(alist: list[int], elem: int) -> int | None:
    lo, hi = 0, len(alist) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if elem == alist[mid]:
            return elem

        elif elem < alist[mid]:
            hi = mid - 1

        else:
            lo = mid + 1

    return None

print(binary_search(alist, 13))
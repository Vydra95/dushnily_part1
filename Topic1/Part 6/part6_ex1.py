alist = [1, 3, 5, 6, 28]


def binary_search(alist: list[int], elem: int) -> int | None:
    lo, hi = 0, len(alist) - 1

    try:
        while lo <= hi:
            mid = (lo + hi) // 2

            if elem == alist[mid]:
                return alist.index(elem)

            elif elem < alist[mid]:
                hi = mid - 1

            else:
                lo = mid + 1

        return None
    except TypeError:
        return None


print(binary_search(alist, 6))

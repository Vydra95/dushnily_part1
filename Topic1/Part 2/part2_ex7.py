def find_sum_product(a: int):
    try:
        a1 = a // 10
        a2 = a % 10
        sum_a = a1 + a2
        product_a = a1 * a2
        return sum_a, product_a
    except (TypeError, ValueError):
        return "It's not a number"


print(find_sum_product(25))

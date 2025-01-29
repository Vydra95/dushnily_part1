"""Какое максимальное число идущих подряд равных друг другу элементов?"""

numbers = [
    16,
    21,
    21,
    7,
    7,
    85,
    79,
    79,
    79,
    0,
]
a = 1
maxx = 1
counter = 1

while a < len(numbers):
    if numbers[a] == numbers[a - 1]:
        counter += 1
    else:
        if counter > maxx:
            maxx = counter

        counter = 1

    a += 1

if counter > maxx:
    maxx = counter

print(maxx)

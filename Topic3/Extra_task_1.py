"""Второй по величине элемент последовательности"""

numbers = [16, 21, 7, 5, 32, 0]

max1 = numbers[0]
max2 = numbers[1]

if max2 > max1:
    max1, max2 = max2, max1

i = 2
while i < len(numbers):
    if numbers[i] > max1:
        max2 = max1
        max1 = numbers[i]
    elif numbers[i] > max2:
        max2 = numbers[i]

    i += 1

print(max2)

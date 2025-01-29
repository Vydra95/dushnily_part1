"""Второй по величине элемент последовательности"""

numbers = [21, 16, 7, 5, 0]

# Версия "Какая-то херь, но работает"
x = 1
found = False

while not found:
    for num in range(len(numbers)):
        if x != numbers[num] and num < len(numbers):
            num += 1
        else:
            found = True
            print(x)
    x += 1


# Версия "Ну типа норм"
x1 = numbers[0]
x2 = numbers[1]
a = 1

while a < (len(numbers) - 1):
    if x1 < x2:
        numbers[0] = x1
    else:
        numbers[0] = x2
        numbers[1] = x1
        x1 = numbers[0]
    x2 = numbers[a + 1]
    a += 1

print(x1)

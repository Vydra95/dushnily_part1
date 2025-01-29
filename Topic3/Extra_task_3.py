"""Сколько идущих подряд элементов равны друг другу?"""

numbers = [16, 21, 21, 21, 7, 7, 85, 79, 79, 79, 0]
a = 0
counter = 0

while a < (len(numbers) - 2):
    if numbers[a] != numbers[a + 1] and numbers[a + 1] == numbers[a + 2]:
        counter += 2
        a += 1
    elif numbers[a] == numbers[a + 1] and numbers[a + 1] == numbers[a + 2]:
        counter += 1
        a += 1
    else:
        a += 1

print(counter)

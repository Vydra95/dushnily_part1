"""Список с разными значениями, пройтись по нему в цикле и вывести на экран.
(То же самое со словарем и выведите ключ и значение)"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_dict = {"key1": 1, "key2": 2, "key3": 3}

for i in range(len(my_list)):
    my_list[i] = my_list[i] ** 2

for i in my_dict:
    my_dict[i] **= 2


print(my_list)
print(my_dict)

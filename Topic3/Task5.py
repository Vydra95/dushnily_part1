"""Список с разными значениями, пройтись по нему в цикле и вывести на экран.
(То же самое со словарем и выведите ключ и значение)"""

my_list = [1, 2, 3]
my_dict = {"key1": 1, "key2": 2, "key3": 3}


def change_list(my_list):
    try:
        for i in range(len(my_list)):
            my_list[i] = my_list[i] ** 2
        return my_list
    except TypeError:
        return "It's not a list"


def change_dict(my_dict):
    try:
        for i in my_dict:
            my_dict[i] **= 2
        return my_dict
    except (TypeError, IndexError):
        return "It's not a dict"


print(change_list(my_list))
print(change_dict(my_dict))

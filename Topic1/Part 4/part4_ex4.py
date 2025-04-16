my_list = ["a", "s", "1", "a", "32", "23"]
my_list.sort()


def separate_lists(my_list):
    letters = my_list[3:6]
    letters.pop()
    letters.reverse()
    return letters


print(separate_lists(my_list))

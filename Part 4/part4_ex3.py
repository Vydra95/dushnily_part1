my_list = ['a', 's', '1', 'a', '32','23']
my_list.sort()

def separate_lists(my_list):
    list_a = my_list[0:3]
    list_b = my_list[3:6]
    return list_a, list_b

print(separate_lists(my_list))
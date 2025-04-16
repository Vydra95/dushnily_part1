my_list = [1, 2]


def hunt_list(my_list):
    try:
        if isinstance(my_list, list):
            first = my_list[0]
            third = my_list[2]
            find_slice = my_list[0:3]
            return first, third, find_slice
        else:
            return "It's not a list"
    except IndexError:
        return "Your list is too short"


print(hunt_list(my_list))

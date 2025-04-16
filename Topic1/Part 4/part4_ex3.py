my_list = ["Cecilia", "Abigail", "Dorothy", 464, 3, 23]


def separate_lists(my_list):
    try:
        if isinstance(my_list, list) and len(my_list) == 6:
            my_list.sort()
            list_a = my_list[0:3]
            list_b = my_list[3:6]
            return list_a, list_b
        else:
            raise TypeError
    except (TypeError, ValueError, IndexError):
        return "Something's wrong"


print(separate_lists(my_list))

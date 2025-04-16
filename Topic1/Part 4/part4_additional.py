my_list = [1, 23, 84, 81, 90]
your_list = 11


def merge_change(my_list, your_list):
    try:
        my_list.extend(your_list)
        my_list.insert(len(my_list), "wow")
        return my_list
    except (TypeError, ValueError):
        return "Can't merge that"


print(merge_change(my_list, your_list))

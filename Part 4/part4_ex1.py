my_list = [1, 2, 3, 4, 5]

def hunt_list():
    first = my_list[0]
    third = my_list[2]
    find_slice = my_list[0:3]
    return first, third, find_slice

print('Первый - ', hunt_list()[0], ', Третий - ', hunt_list()[1], ', Срез - ', hunt_list()[2])
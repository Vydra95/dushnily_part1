city = ['Ростов', '+', 'на', '-', 'Дону']

def correct_name(city):
    city[1] = '-'
    return city

print(correct_name(city))
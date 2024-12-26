data = {'name': 'Bob', 'age': 37, 'gender': 'male', 'height': 185, 'weight': 98, 'occupation': 'plumber', 'car': 'Toyota'}

def find_key(b):
    a = data.get(b)
    return a

print(find_key('address'))

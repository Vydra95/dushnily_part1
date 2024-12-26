data = {'name': 'Bob', 'age': 37, 'gender': 'male', 'height': 185, 'weight': 98, 'occupation': 'plumber', 'car': 'Toyota'}

def update_key(b, n):
    data[b] = [data.get(b)]
    data[b].append(n)
    return data

print(update_key('car', 'Honda'))

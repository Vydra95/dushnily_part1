data = {
    "name": "Bob",
    "age": 37,
    "gender": "male",
    "height": 185,
    "weight": 98,
    "occupation": "plumber",
    "car": "Toyota",
}


def find_key(data, b):
    try:
        a = data.get(b)
        return a
    except AttributeError:
        return None


print(find_key(data, 3.05))

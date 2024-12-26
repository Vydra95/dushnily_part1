data = [('name', 'Bob'), ('age', 37), ('gender', 'male'), ('height', 185), ('weight', 98)]
patient = dict(data)

print(patient)

patient['shoe size'] = 42

print(patient)

patient.pop('age')

print(patient)

data1 = [('name', 'Bob'), ('age', 37), ('gender', 'male'), ('height', 185), ('weight', 98)]
data2 = [('occupation', 'plumber'), ('car', 'Toyota')]

patient_a = dict(data1)

patient_a.update(dict(data2))

print(patient_a)
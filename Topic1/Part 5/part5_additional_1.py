main_data = [("name", "Bob"), ("age", 37), ("gender", "male"), ("height", 185), ("weight", 98)]
new_data = [("occupation", "plumber"), ("car", "Toyota")]


def patient_update(main_data, new_data):
    try:
        patient_a = dict(main_data)
        patient_a.update(dict(new_data))
        return patient_a
    except (TypeError, ValueError):
        return "Can't update"


print(patient_update(main_data, new_data))

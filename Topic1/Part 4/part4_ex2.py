city = ["Ростов", "+", "на", "-", "Дону"]


def correct_name(city):
    try:
        if isinstance(city, list):
            city[1] = "-"
            city = "".join(city)
            return city
        else:
            return "Can't change that"
    except (TypeError, ValueError, IndexError):
        return "Something's wrong"


print(correct_name(city))

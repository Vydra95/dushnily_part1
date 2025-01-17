city = input()


def location() -> str:
    data = {
        "London": (51.5072, 0.1276),
        "Paris": (48.8575, 2.3514),
        "New York": (40.7128, 74.0060),
        "Tokyo": (35.6764, 139.6500),
    }
    try:
        value = data[city]
        return f"{value}"
    except KeyError:
        return "unknown by coordinates"
    finally:
        print("your city is")


print(location())

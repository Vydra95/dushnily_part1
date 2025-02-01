"""Движение робота"""


def robot_moves() -> str:
    c = "север"
    n = -1
    match n:
        case 1:
            match c:
                case "север":
                    return "запад"
                case "юг":
                    return "восток"
                case "запад":
                    return "юг"
                case "восток":
                    return "север"
                case _:
                    return "Неизвестное направление"

        case -1:
            match c:
                case "север":
                    return "восток"
                case "юг":
                    return "запад"
                case "запад":
                    return "север"
                case "восток":
                    return "юг"
                case _:
                    return "Неизвестное направление"
        case 0:
            match c:
                case "север":
                    return "север"
                case "юг":
                    return "юг"
                case "восток":
                    return "восток"
                case "запад":
                    return "запад"
                case _:
                    return "Неизвестное направление"
        case _:
            return "Неизвестное направление"


print(robot_moves())

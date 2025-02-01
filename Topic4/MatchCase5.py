"""Описание числа"""


def name_your_number() -> str:
    num = 919
    n1 = num // 100
    n2 = num // 10 - ((num // 100) * 10)
    n3 = num % 10

    if num < 100 or num > 999:
        return "Что-то не так"
    match n1:
        case 1:
            n1 = "сто"
        case 2:
            n1 = "двести"
        case 3:
            n1 = "триста"
        case 4:
            n1 = "четыреста"
        case 5:
            n1 = "пятьсот"
        case 6:
            n1 = "шестьсот"
        case 7:
            n1 = "семьсот"
        case 8:
            n1 = "восемьсот"
        case 9:
            n1 = "девятьсот"
        case _:
            print("Что-то не так")
    match n3:
        case 0:
            n3 = None
        case 1:
            n3 = "один"
        case 2:
            n3 = "два"
        case 3:
            n3 = "три"
        case 4:
            n3 = "четыре"
        case 5:
            n3 = "пять"
        case 6:
            n3 = "шесть"
        case 7:
            n3 = "семь"
        case 8:
            n3 = "восемь"
        case 9:
            n3 = "девять"
        case _:
            print("Что-то пошло не так")
    match n2:
        case 0:
            n2 = None
        case 1:
            match n3:
                case "один":
                    n2 = ""
                    n3 = "одиннадцать"
                case "два":
                    n2 = ""
                    n3 = "двенадцать"
                case "три":
                    n2 = ""
                    n3 = "тринадцать"
                case "четыре":
                    n2 = ""
                    n3 = "четырнадцать"
                case "пять":
                    n2 = ""
                    n3 = "пятнадцать"
                case "шесть":
                    n2 = ""
                    n3 = "шестнадцать"
                case "семь":
                    n2 = ""
                    n3 = "семнадцать"
                case "восемь":
                    n2 = ""
                    n3 = "восемнадцать"
                case "девять":
                    n2 = ""
                    n3 = "девятнадцать"
                case _:
                    print("Что-то пошло не так")
        case 2:
            n2 = "двадцать"
        case 3:
            n2 = "тридцать"
        case 4:
            n2 = "сорок"
        case 5:
            n2 = "пятьдесят"
        case 6:
            n2 = "шестьдесят"
        case 7:
            n2 = "семьдесят"
        case 8:
            n2 = "восемьдесят"
        case 9:
            n2 = "девяносто"
        case _:
            print("Что-то пошло не так")

    return " ".join(str(x) for x in filter(None, [n1, n2, n3]))


print(name_your_number())

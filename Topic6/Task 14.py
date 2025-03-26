"""
Напишите код, в котором будет намерено нарушены все принципы SOLID по одному на каждый пример
# Потом пример кода с исправлением нарушения
"""

"""
S - single responsibility principle
Задача - проверка срока годности продукта в зависимости от его типа
Dairy отвечал за всё подряд - теперь отвечает за принятие аргументов, а остальную работу делают отдельные классы
"""
"""
Нарушено
"""
# STDLIB
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from math import ceil


class Dairy:
    def __init__(self, p_type, exp_date):
        self.p_type = p_type
        self.exp_date = datetime.strptime(exp_date, "%d-%m-%Y")
        self.p_time = None

    def check_p_type(self):
        match self.p_type:
            case "cheese":
                self.p_time = 15
            case "milk" | "kefir":
                self.p_time = 3
            case "yoghurt" | "yogurt":
                self.p_time = 25
            case "cottage cheese":
                self.p_time = 50
            case "cream":
                self.p_time = 1.5
            case "ice-cream" | "icecream" | "ice cream":
                self.p_time = 30
            case "butter":
                self.p_time = 150
            case _:
                self.p_time = None
        return self.p_time

    def check_date(self, current_date):
        self.current_date = datetime.strptime(current_date, "%d-%m-%Y")
        self.time_difference = self.exp_date - self.current_date
        try:
            if self.time_difference > timedelta(days=self.p_time):
                return "It's expired"
            else:
                return "It's still fresh"
        except TypeError:
            return "Don't know"


almette = Dairy("ryajenka", "30-07-2025")
print(almette.check_date("03-07-2025"))

"""
Типа исправлено
"""


class Dairy:
    def __init__(self, p_type, exp_date):
        self.p_type = p_type
        self.exp_date = datetime.strptime(exp_date, "%d-%m-%Y")

    def date_check(self, current_date):
        checker = CheckDate(self.p_type, self.exp_date)
        checker.check_date(current_date)


class CheckDairyType:
    def __init__(self, p_type):
        self.p_type = p_type

    def check_p_type(self):
        match self.p_type:
            case "cheese":
                self.p_time = 15
            case "milk" | "kefir":
                self.p_time = 3
            case "yoghurt" | "yogurt":
                self.p_time = 25
            case "cottage cheese":
                self.p_time = 50
            case "cream":
                self.p_time = 1.5
            case "ice-cream" | "icecream" | "ice cream":
                self.p_time = 30
            case "butter":
                self.p_time = 150
            case _:
                self.p_time = None
        return self.p_time


class CheckDate:
    def __init__(self, p_type, exp_date):
        self.p_type = p_type
        self.exp_date = exp_date
        self.p_time = CheckDairyType(p_type).check_p_type()

    def check_date(self, current_date):
        current_date = datetime.strptime(current_date, "%d-%m-%Y")
        time_difference = self.exp_date - current_date
        if self.p_time is None:
            print("Don't know")
        elif time_difference > timedelta(days=self.p_time):
            print("It's expired")
        else:
            print("It's still fresh")


danissimo = Dairy("yoghurt", "01-03-2025")
danissimo.date_check("21-03-2025")

"""
O - open-close principle
Задача - рассадить людей по транспорту
Раньше пришлось бы переписывать часть класса Accommodation, чтобы добавить новое транспортное средство
или дополнить логику подсчёта транспорта - теперь это отдельные классы, наследуемые от абстрактного,
а методы вынесены в отдельные классы, чтобы следовать принципу DRY
"""
"""
Нарушено
"""


class Accommodation:
    def __init__(self, type, people):
        self.type = type
        try:
            self.people = int(people)
        except ValueError:
            print("People must be presented in numbers")
            pass

    def count_vehicles(self):
        match self.type:
            case "car":
                if self.people >= 3:
                    return ceil(self.people / 3)
                else:
                    return 1
            case "bus":
                if self.people >= 20:
                    return ceil(self.people / 20)
                else:
                    return 1
            case "coach":
                if self.people >= 40:
                    return ceil(self.people / 40)
                else:
                    return 1
            case "train_carriage":
                if self.people >= 50:
                    return ceil(self.people / 50)
                else:
                    return 1
            case _:
                return "Non-valid transport"


trip1 = Accommodation("car", 20)
print(trip1.count_vehicles())
trip2 = Accommodation("coach", 161)
print(trip2.count_vehicles())
trip3 = Accommodation("laika", "crowd")
print(trip3.count_vehicles())

"""
Правильнее
"""


class Accommodation(ABC):
    @abstractmethod
    def count_vehicles(self, people):
        pass


class Cars(Accommodation):
    def __init__(self):
        self.capacity = 3

    def count_vehicles(self, people):
        res = VehicleNumber(people)
        return res.count_vehicles(self.capacity)


class Buses(Accommodation):
    def __init__(self):
        self.capacity = 20

    def count_vehicles(self, people):
        res = VehicleNumber(people)
        return res.count_vehicles(self.capacity)


class Coaches(Accommodation):
    def __init__(self):
        self.capacity = 40

    def count_vehicles(self, people):
        res = VehicleNumber(people)
        return res.count_vehicles(self.capacity)


class TrainCarriages(Accommodation):
    def __init__(self):
        self.capacity = 50

    def count_vehicles(self, people):
        res = VehicleNumber(people)
        return res.count_vehicles(self.capacity)


class People:
    def __init__(self, people):
        self.people = people

    def isit_number(self):
        try:
            self.people = int(self.people)
            return self.people
        except ValueError:
            print("People must be presented in numbers")
            return


class VehicleNumber:
    def __init__(self, people):
        self.people = people

    def count_vehicles(self, capacity):
        occupied = People(self.people)
        people = occupied.isit_number()
        if people:
            if people >= capacity:
                print(ceil(people / capacity))
            else:
                print(1)
        else:
            return


needed_cars = Cars()
needed_cars.count_vehicles(40)
needed_buses = Buses()
needed_buses.count_vehicles("Maria")

"""
L - Liskov substitution principle
"""
"""
Раньше MP3Player наследовался от общего класса Device, поэтому должен иметь то же поведение на make_a_call
Теперь MP3Player наследуется от NonCallableDevice, поэтому метода start_call у него вообще нет
и attribute error нам намекает, что мы взаимодействуем не с тем интерфейсом
"""
"""
Нарушено
"""


class Device:
    pass


class MobilePhone(Device):
    def start_call(self):
        print("Rrrrrinnggg!")


class MP3player(Device):
    def start_call(self):
        raise Exception("Can't call from this device")

    def start_music(self):
        print("Random Song")


def make_a_call(device: Device):
    device.start_call()


Samsung = MobilePhone()
Ipod = MP3player()
make_a_call(Samsung)
make_a_call(Ipod)

"""
Исправлено
"""


class CallableDevice:
    def start_call(self):
        pass


class NonCallableDevice:
    def start_action(self):
        pass


class MobilePhone(CallableDevice):
    def start_call(self):
        print("Rrrrrinnggg!")


class MP3player(NonCallableDevice):
    def start_action(self):
        print("Random Song")


def make_a_call(device: CallableDevice):
    device.start_call()


Samsung = MobilePhone()
Ipod = MP3player()
make_a_call(Samsung)
make_a_call(Ipod)

"""
I - interface segregation principle
"""
"""
Был общий интерфейс с кучей методов - разделила на несколько, чтобы не было неиспользованных методов
"""
"""
Нарушено
"""


class BankAccount(ABC):

    @abstractmethod
    def withdraw(self, sum):
        pass

    @abstractmethod
    def deposit(self, sum):
        pass

    @abstractmethod
    def transfer(self, sum):
        pass


class SavingsAccount(BankAccount):
    def withdraw(self, sum):
        print(f"Withdrawing {sum}...")

    def deposit(self, sum):
        print(f"Depositing {sum}...")

    def transfer(self, sum):
        pass


Abby = SavingsAccount()
Abby.deposit(300)

"""Исправлено"""


class Depositable(ABC):
    @abstractmethod
    def deposit(self, sum):
        pass


class Withdrawable(ABC):
    @abstractmethod
    def withdraw(self, sum):
        pass


class Transferable(ABC):
    @abstractmethod
    def transfer(self, sum):
        pass


class SavingsAccount(Depositable, Withdrawable):
    def withdraw(self, sum):
        print(f"Withdrawing {sum}...")

    def deposit(self, sum):
        print(f"Depositing {sum}...")


Ben = SavingsAccount()
Ben.withdraw(50)

"""
D - dependency inversion principle
"""
"""
Раньше Caller опирался на конкретную реализацию класса Connection, поэтому при изменении класса Connection
(если мы хотим дописать логику отправки сообщений, например), пришлось бы переписывать и Caller
В новой версии и Caller, и Messenger наследуются от абстрактного класса ConnectionService, а Connection опирается на
него и может принимать любые виды сервисов связи
"""
"""
Нарушено
"""


class Connection:
    def make_a_call(self, number):
        print(f"Dialing {number}...")


class Caller:
    def __init__(self):
        self.caller = Connection()

    def via_call(self, number):
        self.caller.make_a_call(number)


connection1 = Caller()
connection1.via_call("88005553535")

"""Исправлено"""


class ConnectionService(ABC):
    @abstractmethod
    def connect(self, something):
        pass


class Caller(ConnectionService):
    def connect(self, number):
        print(f"Dialing {number}...")


class Messenger(ConnectionService):
    def connect(self, person):
        print(f"Sending a message to {person}...")


class AConnection:
    def __init__(self, service: ConnectionService):
        self.service = service

    def connect(self, something):
        self.service.connect(something)


calling = Caller()
interacting1 = AConnection(calling)
interacting1.connect("12345")
messaging = Messenger()
interacting2 = AConnection(messaging)
interacting2.connect("Julia")

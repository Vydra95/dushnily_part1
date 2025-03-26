"""
Множественное наследование и super
"""


class VerifyPassport:
    def __init__(self, text):
        self.tokens = text.split()
        if len(self.tokens) != 6:
            raise SystemExit("Wrong Passport Data")


class VerifyName(VerifyPassport):
    def __init__(self, text):
        super().__init__(text)
        self.name_check = self.name_validity()

    def name_validity(self):
        self.names = [self.tokens[0], self.tokens[1], self.tokens[2]]
        for i in range(len(self.names) - 1):
            if not isinstance(self.names[i], str):
                res = "Non-valid name"
                break
            if len(self.names[i]) < 2 or len(self.names[i]) > 50:
                res = "Non-valid name"
                break
            else:
                res = "Valid name"
        return res


class VerifyDateOfBirth(VerifyPassport):
    def __init__(self, text):
        super().__init__(text)
        self.date_check = self.date_validity()

    def date_validity(self):
        self.date = [self.tokens[3], self.tokens[4], self.tokens[5]]
        try:
            self.date = [int(x) for x in self.date]
        except ValueError:
            print("Non-valid data")
            return ""
        for i in range(len(self.date) - 1):
            int(self.date[i])
        if not 0 < self.date[0] < 32:
            ress = "Non-valid data"
            return ress
        if not 0 < self.date[1] < 13:
            ress = "Non-valid data"
            return ress
        if not 1900 < self.date[2] < 2012:
            ress = "Non-valid data"
            return ress
        else:
            ress = "Valid data"
            return ress


class Resolution(VerifyName, VerifyDateOfBirth):
    def __init__(self, text):
        super().__init__(text)


pt = Resolution("Ivanov Dmitrii Petrovich 30 7 2000")
print(pt.name_check)
print(pt.date_check)

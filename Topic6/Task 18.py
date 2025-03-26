"""
Полностью неизменяемый Singleton + хэшируемость
"""


class DigitalSignature:
    __instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DigitalSignature.__instance = None

    def __init__(self, value):
        if not self._initialized:
            self.value = value
            DigitalSignature._initialized = True

    def __setattr__(self, key, value):
        if self._initialized and key != "_initialized":
            raise AttributeError(f"Cannot modify attribute '{key}' after initialization")
        super().__setattr__(key, value)

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value


sign1 = DigitalSignature("l435gd93")
print(sign1.value)
sign2 = DigitalSignature("fkrh398dd227")
print(sign2.value)
print(sign1 == sign2)
print(hash(sign1))
print(hash(sign2))

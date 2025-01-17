# STDLIB
from dataclasses import dataclass


@dataclass
class Variables:
    a: int
    b: int
    c: int


variables = Variables(a=1, b=2, c=3)
attr_name = input()
try:
    value = getattr(variables, attr_name)
    print(value)
except AttributeError:
    print("Not in Variables")

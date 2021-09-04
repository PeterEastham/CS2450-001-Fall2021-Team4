"""
Allows us to use Integer Comparision instead of String Comparision, beyond
that we can easily add in more Methods without changing IF Statements.
"""
from enum import Enum, unique

@unique
class Paycheck_Method(Enum):
    DIRECT_DEPOSIT = 1
    MAIL = 2

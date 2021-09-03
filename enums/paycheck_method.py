from enum import Enum, unique

@unique
class Paycheck_Method(Enum):
    DIRECT_DEPOSIT = 1
    MAIL = 2

"""
Abstracting out the values improves the readablity of the code.
Enums are useful for this.
"""
from enum import Enum, unique

@unique
class Paycheck_Method(Enum):
    DIRECT_DEPOSIT = 1
    MAIL = 2
    #Copying CS1410's values for backward compatibility.

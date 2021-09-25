"""
By abstracting out the values from the definition, we can improve readability of
the code base.
"""
from enum import Enum, unique
@unique
class Classification(Enum):
    HOURLY = 1
    SALARIED = 2
    COMMISSIONED = 3
    #Values copy the CS1410 ones for backwards compatibility.

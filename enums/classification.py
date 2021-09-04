"""
Allows us to use Integer Comparision (Slightly Faster) while programming in English
"""
from enum import Enum, unique
@unique
class Classification(Enum):
    SALARIED = 1
    COMMISSIONED = 2
    HOURLY = 3

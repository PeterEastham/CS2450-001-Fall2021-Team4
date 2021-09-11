"""
Allows us to use Integer Comparision (Slightly Faster) while programming in English
"""
from enum import Enum, unique
@unique
class Classification(Enum):
    HOURLY = 1
    SALARIED = 2
    COMMISSIONED = 3

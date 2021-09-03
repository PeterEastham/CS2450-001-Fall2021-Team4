from enum import Enum, unique
@unique
class Classification(Enum):
    SALARIED = 1
    COMMISSIONED = 2
    HOURLY = 3

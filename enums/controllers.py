"""
For readability we'll reference different controller types in
controller_controller.Controller using this Enum
"""

from enum import Enum, unique
@unique
class Controller_Types(Enum):
    EMPLOYEE_CONTROLLER = 1
    PAYMENT_CONTROLLER = 2
    RECEIPT_CONTROLLER = 3
    TIMECARD_CONTROLLER = 4
    USER_CONTROLLER = 5
    LOGIN_CONTROLLER = 6
    ROLE_CONTROLLER = 7

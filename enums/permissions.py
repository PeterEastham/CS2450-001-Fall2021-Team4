"""
Employees will keep an internal Array of Permissions.
We will use this to improve Code Readability
"""

from enum import Enum, unique

@unique
class Permission(Enum):
    MAKE_PAYROLL = 1
    CAN_VIEW_EMP = 2
    CAN_CREATE_USER = 3
    CAN_GIVE_PERM = 4

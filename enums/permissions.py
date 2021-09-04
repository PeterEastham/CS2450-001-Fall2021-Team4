"""
Employees will keep an internal Array of Permissions.
We will use this to improve Code Readability
"""

from enum import Enum, unique

@unique
class Permission(Enum):
    ADMIN = 1
    CAN_VIEW_EMP = 2

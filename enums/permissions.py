"""
Employees will keep an internal Array of Permissions.
Easiest to use an Enum to keep track of differences.
POTENTIALLY could put the permissions into a
.csv database so you could give them a display name.
Likely will just stick that as a dictionary in this file though.
"""

from enum import Enum, unique

@unique
class Permission(Enum):
    MAKE_PAYROLL = 1
    CAN_VIEW_EMP = 2
    CAN_CREATE_USER = 3
    CAN_GIVE_PERM = 4

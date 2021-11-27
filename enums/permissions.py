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
    CAN_VIEW_BSC_EMP_INFO = 5
    CAN_VIEW_ADV_EMP_INFO = 6
    CAN_CHANGE_OTHER_EMP_INFO = 7
    CAN_EXPORT_DATABASE = 8
    PROVIDE_ONE_TIME_PASSWORD = 9


display_name = {
    1 : "Make Payroll",
    3 : "Create User",
    4 : "Give Permission",
    6 : "View Employee Information",
    7 : "Edit Other Employees",
}

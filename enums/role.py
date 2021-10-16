"""
Used as a wrapper for Permissions, we can grant bulk access to permissions using
the Role of the User.

We can limit different Permissions by cross-role validation. Examples.
Supervisor can edit Employee Below them.
Manager can edit Supervisors/Employee below them.
Supervisor cannot edit a Manager.

This Enum will hold the different Roles, while
the role_controller will handle that logic.
"""

from enum import Enum, unique

@unique
class Role(Enum):
    BASIC_EMP = 1
    HUMAN_RESOURCE = 2
    SUPERVISOR = 3
    ACCOUNTING = 4
    MANAGEMENT = 5

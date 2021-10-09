"""
Since Employee != User, we'll use this.
It also allows us to not need to read in the Employee Database until we have to.

"""
class User:

    def __init__(self, username, password, employee_id, permissions):
        self.username = username
        self.password = password
        self.employee_id = employee_id
        self.permissions = self.parsePermissions(permissions)


    #Swap list for a map? O(n) to 1
    def has_permission(self, permission):
        return permission in self.permissions

    def get_id(self):
        return employee_id

    #Allow permissions to be a pre-computed int list?
    def parsePermissions(self, permissions):
        if len(permissions) == 0:
            return list()
        permissions = permissions.split(":")
        temp = list()
        for permission in permissions:
            temp.append(int(permission))
        return temp


    def save_format(self):
        save = ""
        save += self.username
        save += ","
        save += self.password
        save += ","
        save += self.employee_id
        save += ","

        for permission in self.permissions:
            save += f"{permission}:"

        if save[-1:] == ":":
            save = save[:-1]
        save += '\n'
        return save
